import io
import json
import unittest
from unittest.mock import call, patch

from datetime import timezone, timedelta

from sync_anki_progress import (
    aggregate_daily_reviews, collect_summary, flatten_review_events, merge_daily_history, request_json,
)


class FlattenReviewEventsTests(unittest.TestCase):
    def test_flat_list(self):
        rows = [{"id": 1700000000000, "ease": 3, "type": 1}]
        self.assertEqual(flatten_review_events(rows), rows)

    def test_card_id_to_events_mapping(self):
        rows = flatten_review_events({
            "123": [{"id": 1700000000000, "ease": 4, "type": 1}]
        })
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0]["cardId"], "123")
        self.assertEqual(rows[0]["ease"], 4)

    def test_card_grouped_response(self):
        rows = flatten_review_events([
            {"cardId": 456, "reviews": [
                {"id": 1700000000000, "ease": 1, "type": 0},
                {"id": 1700000001000, "ease": 3, "type": 1}
            ]}
        ])
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["cardId"], 456)

    def test_empty_response(self):
        self.assertEqual(flatten_review_events(None), [])
        self.assertEqual(flatten_review_events([]), [])

    def test_unexpected_response_fails_closed(self):
        with self.assertRaises(RuntimeError):
            flatten_review_events("unexpected")



class AggregateDailyReviewsTests(unittest.TestCase):
    def test_aggregates_ease_review_type_and_time(self):
        events = [
            {"id": 1700000000000, "ease": 1, "type": 0, "time": 1200},
            {"id": 1700000001000, "ease": 3, "type": 1, "time": 800},
            {"id": 1700000002000, "ease": 4, "type": 3, "time": 500},
            {"id": 1700000003000, "ease": 2, "type": 2, "time": 300},
        ]
        result = aggregate_daily_reviews(events, timezone.utc)
        day = next(iter(result.values()))
        self.assertEqual(day, {
            "reviews": 4, "again": 1, "hard": 1, "good": 1, "easy": 1,
            "learning_or_relearning": 2, "review": 1, "filtered": 1,
            "time_ms": 2800,
        })

    def test_uses_local_date_for_midnight_boundary(self):
        # 2023-11-14 02:00 UTC is still 2023-11-13 in UTC-6.
        events = [{"id": 1699927200000, "ease": 3, "type": 1, "time": 10}]
        result = aggregate_daily_reviews(events, timezone(timedelta(hours=-6)))
        self.assertIn("2023-11-13", result)

    def test_ignores_events_without_review_id(self):
        self.assertEqual(aggregate_daily_reviews([{"ease": 3}], timezone.utc), {})


class MergeDailyHistoryTests(unittest.TestCase):
    def test_preserves_older_dates_and_replaces_reexported_date(self):
        previous = {"2026-10-30": {"reviews": 5}, "2026-10-31": {"reviews": 7}}
        current = {"2026-10-31": {"reviews": 9}, "2026-11-01": {"reviews": 2}}
        result = merge_daily_history(previous, current)
        self.assertEqual(result, {
            "2026-10-30": {"reviews": 5},
            "2026-10-31": {"reviews": 9},
            "2026-11-01": {"reviews": 2},
        })


class RequestJsonTests(unittest.TestCase):
    def test_json_payload_sets_content_type_and_posts_json(self):
        payload = {"action": "version", "version": 6}
        with patch(
            "sync_anki_progress.urllib.request.urlopen",
            return_value=io.BytesIO(b'{"result": 6, "error": null}'),
        ) as mocked_urlopen:
            response = request_json("http://127.0.0.1:8765", payload)
        request = mocked_urlopen.call_args.args[0]
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(request.get_header("Content-type"), "application/json")
        self.assertEqual(json.loads(request.data.decode("utf-8")), payload)
        self.assertEqual(response["result"], 6)


class CollectSummaryTests(unittest.TestCase):
    @patch("sync_anki_progress.ANKI_DECKS", ["English Plan"])
    @patch("sync_anki_progress.anki")
    def test_requests_deck_stats_for_the_discovered_decks(self, mock_anki):
        mock_anki.side_effect = [
            ["English Plan"],
            {"123": {
                "name": "English Plan", "new_count": 2, "learn_count": 1,
                "review_count": 3, "total_in_deck": 100,
            }},
            [456],
            {"456": [{"id": 1700000000000, "ease": 3, "type": 1, "time": 500}]},
        ]
        summary = collect_summary()
        self.assertEqual(mock_anki.call_args_list[1], call("getDeckStats", decks=["English Plan"]))
        self.assertEqual(summary["decks"]["English Plan"]["total_in_deck"], 100)
        self.assertEqual(sum(x["reviews"] for x in summary["daily_reviews_local_time"].values()), 1)


class DeckScopeTests(unittest.TestCase):
    @patch("sync_anki_progress.ANKI_DECKS", ["English Plan"])
    @patch("sync_anki_progress.anki")
    def test_only_configured_decks_are_queried(self, mock_anki):
        mock_anki.side_effect = [
            ["English Plan", "Personal Deck"],
            {"123": {
                "name": "English Plan", "new_count": 1, "learn_count": 0,
                "review_count": 0, "total_in_deck": 20,
            }},
            [456],
            {"456": []},
        ]
        summary = collect_summary()
        self.assertEqual(mock_anki.call_args_list[1], call("getDeckStats", decks=["English Plan"]))
        self.assertEqual(mock_anki.call_args_list[2], call("findCards", query='deck:"English Plan"'))
        self.assertEqual(list(summary["decks"]), ["English Plan"])

    @patch("sync_anki_progress.ANKI_DECKS", ["Missing Deck"])
    @patch("sync_anki_progress.anki")
    def test_missing_configured_deck_fails_before_collection(self, mock_anki):
        mock_anki.return_value = ["English Plan", "Personal Deck"]
        with self.assertRaisesRegex(RuntimeError, "Configured Anki deck"):
            collect_summary()
        mock_anki.assert_called_once_with("deckNames")


if __name__ == "__main__":
    unittest.main()
