# Anki → local Python → GitHub progress sync

**Status:** implementation draft prepared; not installed or tested against the learner's Mac/Anki collection.  
**Purpose:** publish a small, privacy-conscious progress summary from the learner's local Anki collection to this repository.

## Architecture

1. Anki Desktop runs locally with the AnkiConnect add-on enabled.
2. A local Python script sends JSON-encoded HTTP POST requests to AnkiConnect at `http://127.0.0.1:8765`.
3. The script reads only the configured English deck name(s), their counts, and review events. By default it targets `1000 frases comunes en ingles`; set `ANKI_DECKS` to a comma-separated list of exact deck names to override this.
4. It aggregates review events by local calendar date; current deck counts are reported separately.
5. It uploads only aggregate counts to `learning-data/anki-progress.json` through the GitHub Contents API.
6. ChatGPT can use the committed summary as historical evidence when planning review and conversation transfer.

The local Anki collection remains the source of truth for card scheduling. GitHub is a progress mirror, not a replacement for Anki. AnkiConnect's developer documentation describes a JSON-encoded HTTP POST request containing `action`, `version`, and `params` ([official AnkiConnect documentation](https://github.com/FooSoft/anki-connect#sample-invocation)).

## Data minimisation

The first implementation must not upload:
- card fronts/backs, phrase text, translations, audio, notes, or personal study answers;
- Anki collection files or media;
- API keys, access tokens, or service-account credentials.

The JSON summary contains only sync time, the explicitly configured deck name(s), aggregate counts, daily review counts, and ease-button totals. Other Anki decks are not queried or uploaded by default. The script stops before collecting statistics if the configured deck is missing.

## Requirements

- Anki Desktop running on the Mac.
- AnkiConnect add-on installed and enabled (default local endpoint, port 8765). Keep it bound to `127.0.0.1`; do not expose the API port to the local network or the internet.
- Python 3.10+ (standard library only).
- A GitHub fine-grained token restricted to this repository with **Contents: Read and write**. Do not use a classic broad-scope token.
- Store the token in the macOS Keychain or inject it as the `GITHUB_TOKEN` environment variable at runtime. Never put it in this repository or shell history.

## First-time setup

1. Install AnkiConnect from AnkiWeb and restart Anki.
2. Keep Anki open.
3. Create a fine-grained GitHub token limited to this repository, Contents read/write.
4. Run the script manually with `GITHUB_REPOSITORY=Jchernand3z19/english-90day-study-plan`, `GITHUB_BRANCH=main`, and `GITHUB_TOKEN` set in the process environment. The default deck name is `1000 frases comunes en ingles`; if you renamed it, set `ANKI_DECKS` to the exact name.
5. Inspect the resulting commit and JSON summary.
6. Only after a successful manual test, consider scheduling it with macOS launchd. Do not schedule it yet.

## Manual run

From the repository root:

```bash
GITHUB_REPOSITORY=Jchernand3z19/english-90day-study-plan \
GITHUB_BRANCH=main \
GITHUB_TOKEN='(provide securely at runtime)' \
python3 integrations/anki-github/sync_anki_progress.py
```

Do not paste the real token into chat or commit it to a file. For routine use, prefer a Keychain-backed launcher rather than placing the token directly in a command.

## Safety and failure behaviour

- The script refuses to upload if AnkiConnect is unreachable or required API calls fail.
- It does not create or modify Anki cards.
- It never uploads the raw review log or card text.
- It preserves the existing GitHub file by sending its current blob SHA when updating.
- If GitHub returns a conflict, rerun after checking the repository state; do not force-push.
- The first run is manual. Automatic scheduling is deliberately deferred until the learner has approved the data scope and the manual test succeeds.

## Known limitations

- AnkiConnect must be installed and Anki must be open on the local Mac. Keep the add-on's default localhost-only binding; do not expose its broad collection API to other devices.
- A local process is required; GitHub-hosted runners cannot reach the learner's localhost AnkiConnect service.
- This is a progress mirror only. It does not yet map individual card IDs to conversation turns or claim spoken mastery.
- A card's Anki ease response is not proof of listening comprehension, pronunciation, or independent spoken transfer.
- The 14 unit tests cover JSON request headers/body, configured-deck scoping, empty/missing-deck fail-closed behavior, the required deck-list argument for `getDeckStats`, review-response flattening, aggregate ease/review-type/time counts, local-date boundaries, missing review IDs, and preservation of historical daily totals. They do not replace a live AnkiConnect/GitHub end-to-end test.
- No live Anki connection or token is available in this environment, so the script cannot be end-to-end tested here.
