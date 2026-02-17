"""Test real exercise CLI behavior, including negative starter grading."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
class CliTests(unittest.TestCase):
    def run_cli(self,*args):
        return subprocess.run([sys.executable,str(ROOT/'practice/run.py'),*args],cwd=ROOT,
                              capture_output=True,text=True)
    def test_reference_passes(self):
        self.assertEqual(self.run_cli('reference','E01').returncode,0)
    def test_unfinished_starter_fails(self):
        result=self.run_cli('grade','E01','--submission',str(ROOT/'practice/starters/E01.py'))
        self.assertEqual(result.returncode,1)
        self.assertIn('NotImplementedError',result.stdout)
    def test_boolean_cannot_impersonate_integer(self):
        with tempfile.TemporaryDirectory() as temp:
            submission=Path(temp)/'answer.py'
            submission.write_text('def solve(data):\n    return True\n',encoding='utf-8')
            self.assertEqual(self.run_cli('grade','E01','--submission',str(submission)).returncode,1)
