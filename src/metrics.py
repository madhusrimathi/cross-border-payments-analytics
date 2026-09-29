def compute_metrics(df):
    required = {"amount_sgd", "revenue_sgd", "from_currency", "to_currency"}
    missing = required.difference(df.columns)
    if missing:
        raise ValueError(f"Missing reporting columns: {', '.join(sorted(missing))}")

    corridor_revenue_sgd = (
        df.groupby(["from_currency", "to_currency"])["revenue_sgd"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "total_volume_sgd": df["amount_sgd"].sum(),
        "total_revenue_sgd": df["revenue_sgd"].sum(),
        "avg_ticket_size_sgd": df["amount_sgd"].mean(),
        "avg_revenue_per_txn_sgd": df["revenue_sgd"].mean(),
        "corridor_revenue_sgd": corridor_revenue_sgd,
    }
