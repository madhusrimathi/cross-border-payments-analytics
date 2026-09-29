"""Generate reproducible, illustrative cross-border payment transactions."""
import numpy as np
import pandas as pd

# Fixed teaching assumptions, not live or historical market quotes.
SGD_PER_SOURCE = {"SGD": 1.0, "USD": 1.35, "EUR": 1.47}
TARGET_PER_SGD = {"THB": 26.0, "MYR": 3.4, "IDR": 11500.0}


def generate_transactions(n=1000, seed=42):
    if n < 0:
        raise ValueError("n must be non-negative")

    rng = np.random.default_rng(seed)
    df = pd.DataFrame({
        "user_id": rng.integers(1, 200, n),
        "from_currency": rng.choice(list(SGD_PER_SOURCE), n),
        "to_currency": rng.choice(list(TARGET_PER_SGD), n),
        "amount": rng.uniform(50, 2000, n),
        "fx_spread_percent": rng.uniform(0.3, 1.5, n),
    })
    df["timestamp"] = pd.Timestamp("2024-01-01") + pd.to_timedelta(
        rng.integers(0, 60 * 24 * 30, n), unit="m"
    )
    df["amount_sgd"] = df["amount"] * df["from_currency"].map(SGD_PER_SOURCE)
    df["mid_market_rate"] = (
        df["from_currency"].map(SGD_PER_SOURCE)
        * df["to_currency"].map(TARGET_PER_SGD)
    )
    # A lower target-currency payout represents the provider's FX markup.
    df["customer_rate"] = df["mid_market_rate"] * (1 - df["fx_spread_percent"] / 100)
    df["recipient_amount"] = df["amount"] * df["customer_rate"]
    df["fx_revenue_sgd"] = df["amount_sgd"] * df["fx_spread_percent"] / 100
    return df
