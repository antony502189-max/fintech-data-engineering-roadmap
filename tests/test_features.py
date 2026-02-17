import unittest
from fintech_lab.warehouse import connect,ingest
from fintech_lab.synthetic import payments
from fintech_lab.features import capture_total_at

class FeatureTests(unittest.TestCase):
    def setUp(self): self.db=connect(); ingest(self.db,payments())
    def tearDown(self): self.db.close()
    def test_late_data_is_not_known(self):
        self.assertEqual(capture_total_at(self.db,"p3","USD","2026-01-02T00:00:00Z"),0)
    def test_after_arrival(self):
        self.assertEqual(capture_total_at(self.db,"p3","USD","2026-01-04T00:00:00Z"),2500)
    def test_strict_event_boundary(self):
        self.assertEqual(capture_total_at(self.db,"p1","USD","2026-01-01T12:00:00Z"),0)
    def test_currency_filter(self):
        self.assertEqual(capture_total_at(self.db,"p2","USD","2026-01-05T00:00:00Z"),0)
