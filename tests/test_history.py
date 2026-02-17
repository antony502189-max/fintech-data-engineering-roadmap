import unittest
from fintech_lab.warehouse import connect
from fintech_lab.scd import apply_change,tier_at

class HistoryTests(unittest.TestCase):
    def setUp(self): self.db=connect()
    def tearDown(self): self.db.close()
    def load(self):
        apply_change(self.db,"c1","basic","2026-01-01T00:00:00Z")
        apply_change(self.db,"c1","premium","2026-01-03T00:00:00Z")
    def test_boundary(self):
        self.load()
        self.assertEqual(tier_at(self.db,"c1","2026-01-03T00:00:00Z"),"premium")
        self.assertEqual(tier_at(self.db,"c1","2026-01-02T23:59:59Z"),"basic")
    def test_before_history(self):
        self.load(); self.assertIsNone(tier_at(self.db,"c1","2025-12-31T00:00:00Z"))
    def test_late_change_splits_interval(self):
        self.load(); apply_change(self.db,"c1","plus","2026-01-02T00:00:00Z")
        self.assertEqual(tier_at(self.db,"c1","2026-01-02T12:00:00Z"),"plus")
        rows=self.db.execute("SELECT * FROM customers_history ORDER BY valid_from").fetchall()
        self.assertEqual(rows[0]["valid_to"],rows[1]["valid_from"])
        self.assertEqual(rows[1]["valid_to"],rows[2]["valid_from"])
    def test_replay(self):
        self.load(); self.load()
        self.assertEqual(self.db.execute("SELECT count(*) FROM customers_history").fetchone()[0],2)
    def test_conflicting_change(self):
        self.load()
        with self.assertRaises(ValueError): apply_change(self.db,"c1","other","2026-01-01T00:00:00Z")
        self.assertEqual(tier_at(self.db,"c1","2026-01-01T12:00:00Z"),"basic")
