"""Simple transaction-size flag; this does not predict fraud or risk."""


def apply_risk_scoring(df):
    result = df.copy()
    result["large_payment_flag"] = result["amount_sgd"] > 1500
    return result
