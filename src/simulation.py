import pandas as pd
import numpy as np

def generate_transactions(n=1000):
    np.random.seed(42)

    data = {
        "user_id": np.random.randint(1, 200, n),
        "from_currency": np.random.choice(["SGD", "USD", "EUR"], n),
        "to_currency": np.random.choice(["THB", "MYR", "IDR"], n),
        "amount": np.random.uniform(50, 2000, n),
        "fx_spread_percent": np.random.uniform(0.3, 1.5, n),
    }

    df = pd.DataFrame(data)
    df["revenue"] = df["amount"] * df["fx_spread_percent"] / 100

    return df
