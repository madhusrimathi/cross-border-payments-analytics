import matplotlib.pyplot as plt
from src.simulation import generate_transactions
from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring


def plot_dashboard(df, corridor_revenue_sgd):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    corridor_revenue_sgd.head(5).plot(kind="bar", ax=axes[0])
    axes[0].set_title("Top Revenue Corridors")
    axes[0].set_ylabel("Estimated spread revenue (SGD)")
    axes[0].tick_params(axis="x", rotation=30)

    daily = df.set_index("timestamp")["revenue_sgd"].resample("D").sum()
    daily.plot(ax=axes[1])
    axes[1].set_title("Daily Revenue Trend")
    axes[1].set_ylabel("Estimated spread revenue (SGD)")
    axes[1].set_xlabel("Date")

    plt.tight_layout()
    plt.show()


def main():
    df = apply_risk_scoring(generate_transactions(1000))
    metrics = compute_metrics(df)

    print("Total Payment Volume (SGD):", round(metrics["total_volume_sgd"], 2))
    print("Estimated FX Spread Revenue (SGD):", round(metrics["total_revenue_sgd"], 2))
    print("Average Ticket Size (SGD):", round(metrics["avg_ticket_size_sgd"], 2))
    print("Average Revenue per Transaction (SGD):", round(metrics["avg_revenue_per_txn_sgd"], 2))

    print("\nTop Revenue Corridors (SGD):")
    print(metrics["corridor_revenue_sgd"].head())
    plot_dashboard(df, metrics["corridor_revenue_sgd"])


if __name__ == "__main__":
    main()
