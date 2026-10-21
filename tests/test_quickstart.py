"""Protect the first-session monetary explanation and repeatable CLI behavior."""
from pathlib import Path
import subprocess
import sys
import unittest

from fintech_lab.quickstart import run_demo


class QuickstartTests(unittest.TestCase):
    def test_repeated_sessions_have_independent_state(self):
        for _ in range(2):
            report = run_demo()
            self.assertEqual(report["first"],
                             {"inserted": 6, "duplicates": 0, "quarantined": 0})
            self.assertEqual(report["replay"],
                             {"inserted": 0, "duplicates": 6, "quarantined": 0})
            rows = {row["payment_id"]: row for row in report["reconciliation"]}
            self.assertEqual(rows["p1"]["expected_minor"], 10000 - 300 - 2000)
            self.assertEqual(rows["p1"]["status"], "matched")
            self.assertEqual(rows["p2"]["currency"], "EUR")
            self.assertEqual(rows["p2"]["expected_minor"], 5000 - 100)
            self.assertEqual(rows["p2"]["status"], "matched")
            self.assertEqual(rows["p3"]["delta_minor"], -100)
            self.assertEqual(rows["p3"]["status"], "amount_mismatch")
            self.assertIsNone(rows["p9"]["expected_minor"])
            self.assertIsNone(rows["p9"]["delta_minor"])
            self.assertEqual(rows["p9"]["status"], "unexpected_external")

    def test_documented_command_succeeds_and_explains_exceptions(self):
        result = subprocess.run(
            [sys.executable, "-m", "fintech_lab.quickstart"],
            cwd=Path(__file__).resolve().parents[1],
            capture_output=True, text=True,
        )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("0 inserted, 6 duplicates", result.stdout)
        self.assertIn("amount_mismatch", result.stdout)
        self.assertIn("unexpected_external", result.stdout)
        self.assertIn("$1.00", result.stdout)
