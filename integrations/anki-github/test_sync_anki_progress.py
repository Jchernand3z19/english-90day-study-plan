import unittest

from datetime import timezone, timedelta\n\nfrom sync_anki_progress import (\n    aggregate_daily_reviews, flatten_review_events, merge_daily_history,\n)


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


if __name__ == "__main__":
    unittest.main()
