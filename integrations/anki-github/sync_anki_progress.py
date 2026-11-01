#!/usr/bin/env python3
"""Export aggregate Anki review statistics to this repository.

Requires Anki Desktop + AnkiConnect and a narrowly scoped GitHub token.
No card text, translations, notes, audio, or raw review events are uploaded.
"""
from __future__ import annotations

import base64
import json
import os
import sys
import urllib.error
import urllib.request
from collections import defaultdict
from datetime import datetime, timezone
from typing import Any

ANKI_URL = os.environ.get("ANKI_CONNECT_URL", "http://127.0.0.1:8765")
REPOSITORY = os.environ.get("GITHUB_REPOSITORY", "")
BRANCH = os.environ.get("GITHUB_BRANCH", "main")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
TARGET_PATH = os.environ.get("GITHUB_TARGET_PATH", "learning-data/anki-progress.json")
# Export only the ordered English deck by default; override with comma-separated names if needed.
ANKI_DECKS = [name.strip() for name in os.environ.get(
    "ANKI_DECKS", "1000 frases comunes en ingles"
).split(",") if name.strip()]


def request_json(url: str, payload: dict[str, Any] | None = None,
                 headers: dict[str, str] | None = None,
                 method: str | None = None) -> Any:
    data = None if payload is None else json.dumps(payload).encode("utf-8")
    request_headers = dict(headers or {})
    if payload is not None:
        request_headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=request_headers, method=method)
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read()
    return json.loads(raw.decode("utf-8")) if raw else None


def anki(action: str, **params: Any) -> Any:
    result = request_json(ANKI_URL, {"action": action, "version": 6, "params": params})
    if not isinstance(result, dict) or result.get("error") is not None:
        raise RuntimeError(f"AnkiConnect action {action!r} failed: {result!r}")
    return result.get("result")


def github_headers() -> dict[str, str]:
    return {
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}",
        "X-GitHub-Api-Version": "2022-11-28",
        "User-Agent": "anki-progress-sync",
    }


def load_existing_file(api_url: str) -> tuple[str | None, dict[str, Any]]:
    try:
        current = request_json(api_url + f"?ref={BRANCH}", headers=github_headers())
    except urllib.error.HTTPError as exc:
        if exc.code == 404:
            return None, {}
        raise
    sha = current.get("sha")
    encoded = current.get("content", "")
    decoded = base64.b64decode(encoded).decode("utf-8") if encoded else "{}"
    try:
        return sha, json.loads(decoded)
    except json.JSONDecodeError:
        raise RuntimeError("Existing progress JSON is invalid; refusing to overwrite it.")


def flatten_review_events(raw: Any) -> list[dict[str, Any]]:
    """Accept common AnkiConnect response shapes and return review event objects."""
    if raw is None:
        return []
    if isinstance(raw, dict):
        flattened: list[dict[str, Any]] = []
        for card_id, events in raw.items():
            if isinstance(events, dict):
                events = events.get("reviews", [events])
            for event in events or []:
                if isinstance(event, dict):
                    item = dict(event)
                    item.setdefault("cardId", card_id)
                    flattened.append(item)
        return flattened
    if isinstance(raw, list):
        flattened = []
        for entry in raw:
            if not isinstance(entry, dict):
                continue
            events = entry.get("reviews")
            if isinstance(events, list):
                for event in events:
                    if isinstance(event, dict):
                        item = dict(event)
                        item.setdefault("cardId", entry.get("cardId"))
                        flattened.append(item)
            elif "id" in entry:
                flattened.append(entry)
        return flattened
    raise RuntimeError(f"Unexpected getReviewsOfCards response: {type(raw).__name__}")



def aggregate_daily_reviews(reviews: list[dict[str, Any]], local_tz=None) -> dict[str, dict[str, int]]:
    """Aggregate review events by local date without retaining individual events."""
    if local_tz is None:
        local_tz = datetime.now().astimezone().tzinfo

    daily: dict[str, dict[str, int]] = defaultdict(
        lambda: {"reviews": 0, "again": 0, "hard": 0, "good": 0, "easy": 0,
                 "learning_or_relearning": 0, "review": 0, "filtered": 0,
                 "time_ms": 0}
    )
    for item in reviews:
        # Anki review IDs are Unix milliseconds; convert explicitly from UTC.
        if "id" not in item:
            continue
        reviewed_at = datetime.fromtimestamp(
            int(item["id"]) / 1000, tz=timezone.utc
        ).astimezone(local_tz)
        day = daily[reviewed_at.date().isoformat()]
        day["reviews"] += 1
        ease = int(item.get("ease", 0))
        if ease == 1:
            day["again"] += 1
        elif ease == 2:
            day["hard"] += 1
        elif ease == 3:
            day["good"] += 1
        elif ease == 4:
            day["easy"] += 1
        review_type = int(item.get("type", -1))
        if review_type in (0, 2):
            day["learning_or_relearning"] += 1
        elif review_type == 1:
            day["review"] += 1
        elif review_type == 3:
            day["filtered"] += 1
        day["time_ms"] += int(item.get("time", 0))
    return dict(sorted(daily.items()))


def merge_daily_history(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    """Preserve prior dates while replacing dates re-exported by the current sync."""
    return {**previous, **current}


def collect_summary() -> dict[str, Any]:
    available_decks = anki("deckNames")
    missing_decks = [name for name in ANKI_DECKS if name not in available_decks]
    if missing_decks:
        raise RuntimeError(
            "Configured Anki deck(s) not found: " + ", ".join(missing_decks)
            + ". Set ANKI_DECKS to the exact deck name(s)."
        )
    deck_names = ANKI_DECKS
    deck_stats = anki("getDeckStats", decks=deck_names)
    deck_stats_by_name = {
        item.get("name"): {
            "new_count": item.get("new_count", 0),
            "learn_count": item.get("learn_count", 0),
            "review_count": item.get("review_count", 0),
            "total_in_deck": item.get("total_in_deck", 0),
        }
        for item in (deck_stats or {}).values()
    }

    # Collect card IDs for all decks; only IDs are used locally to query review history.
    card_ids: list[int] = []
    for deck in deck_names:
        escaped = deck.replace("\\", "\\\\").replace('"', '\\"')
        found = anki("findCards", query=f'deck:"{escaped}"') or []
        card_ids.extend(int(card_id) for card_id in found)
    card_ids = sorted(set(card_ids))

    reviews = []
    # AnkiConnect accepts batches; avoid an excessively large request.
    for start in range(0, len(card_ids), 200):
        batch = card_ids[start:start + 200]
        if batch:
            raw_reviews = anki("getReviewsOfCards", cards=batch)
            reviews.extend(flatten_review_events(raw_reviews))

    daily = aggregate_daily_reviews(reviews)


    return {
        "schema_version": 1,
        "synced_at_utc": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": "Anki Desktop via AnkiConnect",
        "repository": REPOSITORY,
        "decks": {
            name: deck_stats_by_name.get(name, {
                "new_count": 0, "learn_count": 0, "review_count": 0,
                "total_in_deck": 0
            })
            for name in sorted(deck_names)
        },
        "daily_reviews_local_time": dict(sorted(daily.items())),
        "privacy": {
            "card_content_uploaded": False,
            "translations_uploaded": False,
            "audio_uploaded": False,
            "raw_review_events_uploaded": False
        }
    }


def main() -> int:
    if not REPOSITORY or "/" not in REPOSITORY:
        print("Set GITHUB_REPOSITORY=owner/repository.", file=sys.stderr)
        return 2
    if not TOKEN:
        print("Set GITHUB_TOKEN securely in the process environment.", file=sys.stderr)
        return 2

    # Fail early with a clear error if AnkiConnect is unavailable.
    try:
        version = anki("version")
        if int(version) < 6:
            raise RuntimeError(f"AnkiConnect API version 6 required; found {version}.")
        summary = collect_summary()
    except Exception as exc:
        print(f"Could not read Anki: {exc}", file=sys.stderr)
        return 1

    api_url = f"https://api.github.com/repos/{REPOSITORY}/contents/{TARGET_PATH}"
    try:
        sha, previous = load_existing_file(api_url)
        # Preserve the complete daily history; refresh current deck counts and sync time.
        merged = dict(previous)
        merged.update(summary)
        previous_days = previous.get("daily_reviews_local_time", {})
        current_days = summary.get("daily_reviews_local_time", {})
        merged["daily_reviews_local_time"] = merge_daily_history(previous_days, current_days)
        body = {
            "message": "Sync aggregate Anki study progress",
            "content": base64.b64encode(
                (json.dumps(merged, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
            ).decode("ascii"),
            "branch": BRANCH,
        }
        if sha:
            body["sha"] = sha
        result = request_json(api_url, body, github_headers(), method="PUT")
        print(f"Updated {TARGET_PATH}; commit: {result['commit']['sha']}")
        print(f"Decks: {len(summary['decks'])}; review dates: {len(summary['daily_reviews_local_time'])}")
        return 0
    except Exception as exc:
        print(f"GitHub sync failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
