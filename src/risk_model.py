import numpy as np

def apply_risk_scoring(df):
    df["risk_flag"] = np.where(df["amount"] > 1500, 1, 0)

    df["risk_score"] = (
        (df["amount"] > 1500).astype(int) +
        (df["fx_spread_percent"] > 1.2).astype(int)
    )

    return df
