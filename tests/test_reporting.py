import unittest

import pandas as pd

from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring
from src.simulation import add_reporting_amounts, generate_transactions


class ReportingTests(unittest.TestCase):
    def test_mixed_currencies_are_converted_before_aggregation(self):
        raw = pd.DataFrame({
            "from_currency": ["SGD", "USD", "EUR"],
            "to_currency": ["MYR", "MYR", "THB"],
            "amount": [100.0, 100.0, 100.0],
            "fx_spread_percent": [1.0, 1.0, 1.0],
        })
        df = add_reporting_amounts(raw)
        metrics = compute_metrics(df)
        self.assertEqual(df["amount_sgd"].tolist(), [100.0, 135.0, 147.0])
        self.assertAlmostEqual(metrics["total_volume_sgd"], 382.0)
        self.assertAlmostEqual(metrics["total_revenue_sgd"], 3.82)
        self.assertAlmostEqual(metrics["corridor_revenue_sgd"].sum(), 3.82)

    def test_unknown_currency_is_rejected(self):
        raw = pd.DataFrame({"from_currency": ["GBP"], "amount": [100.0], "fx_spread_percent": [1.0]})
        with self.assertRaises(ValueError):
            add_reporting_amounts(raw)

    def test_generated_data_and_risk_threshold_use_sgd(self):
        df = apply_risk_scoring(generate_transactions(1000))
        self.assertTrue((df["amount_sgd"] == df["amount"] * df["sgd_per_unit"]).all())
        self.assertTrue((df["risk_flag"] == (df["amount_sgd"] > 1500).astype(int)).all())


if __name__ == "__main__":
    unittest.main()
