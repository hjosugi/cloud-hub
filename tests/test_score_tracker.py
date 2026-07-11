import argparse
import json
import tempfile
import unittest
from pathlib import Path

from scripts.score_tracker import add_attempt, build_report, load_data, readiness, validate_data


class ScoreTrackerTests(unittest.TestCase):
    def base_data(self):
        return {"schema_version": 1, "targets": {"AIP-C01": 85}, "attempts": []}

    def args(self, score=80):
        return argparse.Namespace(
            date="2026-07-11",
            exam="AIP-C01",
            set_name="Practice #1",
            score=score,
            weak_domains="D3,D5",
            notes="first run",
        )

    def test_adds_incrementing_attempts(self):
        data = self.base_data()
        first = add_attempt(data, self.args(80))
        second = add_attempt(data, self.args(88))
        self.assertEqual(1, first["attempt"])
        self.assertEqual(2, second["attempt"])
        self.assertEqual(["D3", "D5"], first["weak_domains"])

    def test_rejects_out_of_range_score(self):
        with self.assertRaises(ValueError):
            add_attempt(self.base_data(), self.args(101))

    def test_readiness_uses_recent_scores(self):
        status, reason = readiness(self.base_data(), "AIP-C01", [75, 86, 88])
        self.assertEqual("要確認", status)
        self.assertIn("目標85%", reason)
        status, _ = readiness(self.base_data(), "AIP-C01", [86, 88, 90])
        self.assertEqual("受験候補", status)

    def test_report_contains_attempt_and_weak_domain(self):
        data = self.base_data()
        add_attempt(data, self.args(88))
        report = build_report(data)
        self.assertIn("88.0%", report)
        self.assertIn("D3, D5", report)

    def test_load_validates_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "scores.json"
            path.write_text(json.dumps(self.base_data()))
            self.assertEqual([], load_data(path)["attempts"])


if __name__ == "__main__":
    unittest.main()
