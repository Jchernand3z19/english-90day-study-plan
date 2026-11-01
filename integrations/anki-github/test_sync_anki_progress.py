import unittest

from sync_anki_progress import flatten_review_events


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


if __name__ == "__main__":
    unittest.main()
