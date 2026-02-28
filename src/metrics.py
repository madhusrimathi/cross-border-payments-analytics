def compute_metrics(df):
    total_volume = df["amount"].sum()
    total_revenue = df["revenue"].sum()
    avg_ticket = df["amount"].mean()
    avg_revenue_per_txn = df["revenue"].mean()

    corridor_revenue = (
        df.groupby(["from_currency", "to_currency"])["revenue"]
        .sum()
        .sort_values(ascending=False)
    )

    return {
        "total_volume": total_volume,
        "total_revenue": total_revenue,
        "avg_ticket_size": avg_ticket,
        "avg_revenue_per_txn": avg_revenue_per_txn,
        "corridor_revenue": corridor_revenue
    }
