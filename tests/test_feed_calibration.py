import unittest

from scripts.feed_calibration import build_report, evaluate, prepare, validate_review


class FeedCalibrationTests(unittest.TestCase):
    def digest(self):
        return {
            "generated_at": "2026-07-11T00:00:00Z",
            "items": [
                {"id": "1", "vendor": "aws", "title": "Retirement", "url": "https://example.com/1", "category": "deprecation", "priority": "今すぐ確認", "score": 90},
                {"id": "2", "vendor": "gcp", "title": "New database", "url": "https://example.com/2", "category": "data", "priority": "今週確認", "score": 60},
            ],
        }

    def test_prepare_preserves_existing_labels(self):
        first = prepare(self.digest(), "2026-07", 2)
        first["items"][0]["actual_category"] = "deprecation"
        second = prepare(self.digest(), "2026-07", 2, first)
        self.assertEqual("deprecation", second["items"][0]["actual_category"])

    def test_evaluates_accuracy_and_urgent_recall(self):
        review = prepare(self.digest(), "2026-07", 2)
        review["items"][0]["actual_category"] = "deprecation"
        review["items"][0]["actual_priority"] = "今すぐ確認"
        review["items"][1]["actual_category"] = "operations"
        review["items"][1]["actual_priority"] = "今すぐ確認"
        metrics = evaluate(review)
        self.assertEqual(0.5, metrics["category_accuracy"])
        self.assertEqual(0.5, metrics["urgent_recall"])
        self.assertEqual(1, metrics["urgent_false_negative"])
        self.assertIn("50.0%", build_report(metrics))

    def test_rejects_unknown_human_label(self):
        review = prepare(self.digest(), "2026-07", 1)
        review["items"][0]["actual_category"] = "unknown"
        with self.assertRaises(ValueError):
            validate_review(review)


if __name__ == "__main__":
    unittest.main()
