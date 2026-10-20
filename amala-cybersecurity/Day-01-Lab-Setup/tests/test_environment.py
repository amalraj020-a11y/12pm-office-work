import json, subprocess, sys, unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
class TestEnvironment(unittest.TestCase):
    def test_verifier(self):
        p=subprocess.run([sys.executable,str(ROOT/"src"/"verify_environment.py")],capture_output=True,text=True,check=True); d=json.loads(p.stdout); self.assertTrue(d["safe_lab_directories"]); self.assertEqual(d["network_testing"],"NOT RUN: Day 1 performs no network requests or scans"); self.assertTrue((ROOT/"evidence"/"environment-check.json").exists())
if __name__=="__main__": unittest.main()