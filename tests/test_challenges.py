"""Exercise the new CLI's positive workflow and its executable negative starters."""
from pathlib import Path
import subprocess
import sys
import unittest
import json

ROOT = Path(__file__).resolve().parents[1]

class ChallengeCliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run([sys.executable, str(ROOT/'challenges/run.py'), *args],
                              cwd=ROOT, capture_output=True, text=True)

    def test_actual_backup_reference_passes(self):
        result = self.run_cli('reference', 'C06')
        self.assertEqual(result.returncode, 0, result.stdout+result.stderr)
        self.assertIn('C06: 4/4 passed', result.stdout)

    def test_unfinished_workflow_fails(self):
        result = self.run_cli('grade', 'C01', '--submission', str(ROOT/'challenges/starters/C01.py'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('NotImplementedError', result.stdout)

    def test_runnable_sql_starter_has_detectable_financial_defects(self):
        result = self.run_cli('grade', 'C07', '--submission', str(ROOT/'challenges/starters/C07.py'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('C07 case 1:', result.stdout)
        self.assertIn('C07 case 2:', result.stdout)
        self.assertNotIn('NotImplementedError', result.stdout)

    def test_migration_keeps_rejected_source_evidence(self):
        from challenges.solutions.C04 import normalize
        from fintech_lab.warehouse import connect, ingest
        source = {'version': 99, 'event_id': 'bad', 'amount': '1.23', 'provider_note': 'SYNTHETIC'}
        db = connect()
        try:
            self.assertEqual(ingest(db, [normalize(source)])['quarantined'], 1)
            payload = json.loads(db.execute('SELECT payload FROM quarantine').fetchone()[0])
            self.assertEqual(payload['rejected_source'], source)
            self.assertEqual(db.execute('SELECT count(*) FROM raw_events').fetchone()[0], 0)
        finally:
            db.close()
