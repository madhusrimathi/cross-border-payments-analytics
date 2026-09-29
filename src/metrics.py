"""Aggregate amounts only after converting them to a common currency."""


def compute_metrics(df):
    corridor_revenue = (
        df.groupby(["from_currency", "to_currency"])["fx_revenue_sgd"]
        .sum()
        .sort_values(ascending=False)
    )
    return {
        "total_volume_sgd": df["amount_sgd"].sum(),
        "total_fx_revenue_sgd": df["fx_revenue_sgd"].sum(),
        "avg_ticket_sgd": df["amount_sgd"].mean() if len(df) else 0.0,
        "avg_fx_revenue_per_txn_sgd": (
            df["fx_revenue_sgd"].mean() if len(df) else 0.0
        ),
        "corridor_revenue_sgd": corridor_revenue,
        "large_payment_flag_rate": df["large_payment_flag"].mean() if len(df) else 0.0,
    }
