import pandas as pd
import numpy as np


# Illustrative, fixed conversion assumptions: SGD per one unit of source currency.
# These are not historical or live quotes.
SGD_PER_UNIT = {"SGD": 1.00, "USD": 1.35, "EUR": 1.47}


def add_reporting_amounts(df):
    result = df.copy()
    result["sgd_per_unit"] = result["from_currency"].map(SGD_PER_UNIT)
    if result["sgd_per_unit"].isna().any():
        raise ValueError("No SGD reporting rate for at least one source currency")
    result["amount_sgd"] = result["amount"] * result["sgd_per_unit"]
    result["revenue_sgd"] = result["amount_sgd"] * result["fx_spread_percent"] / 100
    return result


def generate_transactions(n=1000):
    rng = np.random.default_rng(42)
    data = {
        "user_id": rng.integers(1, 200, n),
        "from_currency": rng.choice(["SGD", "USD", "EUR"], n),
        "to_currency": rng.choice(["THB", "MYR", "IDR"], n),
        "amount": rng.uniform(50, 2000, n),
        "fx_spread_percent": rng.uniform(0.3, 1.5, n),
    }
    df = add_reporting_amounts(pd.DataFrame(data))
    df["timestamp"] = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 60 * 24 * 30, n), unit="m")
    return df
