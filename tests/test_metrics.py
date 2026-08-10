import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gdn2_scaling.metrics import load_metrics, summarize_loss


class MetricsTest(unittest.TestCase):
    def test_primary_table_shape_and_status(self):
        rows = load_metrics(ROOT / "results" / "metrics.csv")
        self.assertEqual(len(rows), 8)
        self.assertEqual({row.experiment for row in rows}, {"30m", "120m"})
        self.assertTrue(all(row.status == "confirmed" for row in rows if row.experiment == "30m"))
        self.assertTrue(all(row.status == "provisional" for row in rows if row.experiment == "120m"))

    def test_confirmed_30m_result_has_three_seeds(self):
        rows = load_metrics(ROOT / "results" / "metrics.csv")
        seeds = {row.seed for row in rows if row.experiment == "30m" and row.model == "gdn2_flat"}
        self.assertEqual(seeds, {1337, 1338, 1339})

        summary = summarize_loss(rows)
        gdn2_mean = summary[("30m", "gdn2_flat")][0]
        transformer_mean = summary[("30m", "transformer")][0]
        self.assertLess(gdn2_mean, transformer_mean)


if __name__ == "__main__":
    unittest.main()
