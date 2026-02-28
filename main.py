import matplotlib.pyplot as plt
from src.simulation import generate_transactions
from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring
import matplotlib.pyplot as plt


def plot_dashboard(df, corridor_revenue):
    fig, axes = plt.subplots(2, 1, figsize=(10, 8))

    corridor_revenue.head(5).plot(kind="bar", ax=axes[0])
    axes[0].set_title("Top Revenue Corridors")
    axes[0].set_ylabel("Revenue")
    axes[0].tick_params(axis="x", rotation=30)

    daily = df.set_index("timestamp")["revenue"].resample("D").sum()
    daily.plot(ax=axes[1])
    axes[1].set_title("Daily Revenue Trend")
    axes[1].set_ylabel("Revenue")
    axes[1].set_xlabel("Date")

    plt.tight_layout()
    plt.show()


def main():
    df = generate_transactions(1000)
    df = apply_risk_scoring(df)

    metrics = compute_metrics(df)

    print("Total Payment Volume:", round(metrics["total_volume"], 2))
    print("Total Revenue:", round(metrics["total_revenue"], 2))
    print("Average Ticket Size:", round(metrics["avg_ticket_size"], 2))
    print("Average Revenue per Transaction:", round(metrics["avg_revenue_per_txn"], 2))

    print("\nTop Revenue Corridors:")
    print(metrics["corridor_revenue"].head())

    # PLOTS
    plot_dashboard(df, metrics["corridor_revenue"])


if __name__ == "__main__":
    main()
