import numpy as np


def apply_risk_scoring(df):
    result = df.copy()
    high_amount = result["amount_sgd"] > 1500
    high_spread = result["fx_spread_percent"] > 1.2
    result["risk_flag"] = np.where(high_amount, 1, 0)
    result["risk_score"] = high_amount.astype(int) + high_spread.astype(int)
    return result
