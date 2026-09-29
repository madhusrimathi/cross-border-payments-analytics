import argparse

from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring
from src.simulation import generate_transactions


def plot_dashboard(df, corridor_revenue):
    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 1, figsize=(10, 8))
    corridor_revenue.head(5).plot(kind="bar", ax=axes[0])
    axes[0].set_title("Top FX Revenue Corridors (SGD)")
    axes[0].set_ylabel("Illustrative FX revenue (SGD)")
    axes[0].tick_params(axis="x", rotation=30)

    daily = df.set_index("timestamp")["fx_revenue_sgd"].resample("D").sum()
    daily.plot(ax=axes[1])
    axes[1].set_title("Daily Illustrative FX Revenue")
    axes[1].set_ylabel("SGD")
    axes[1].set_xlabel("Date")
    fig.tight_layout()
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Synthetic cross-border payment analysis")
    parser.add_argument("--transactions", type=int, default=1000)
    parser.add_argument("--plot", action="store_true", help="Show matplotlib charts")
    args = parser.parse_args()
    df = apply_risk_scoring(generate_transactions(args.transactions))
    metrics = compute_metrics(df)

    print(f"Total payment volume (SGD): {metrics['total_volume_sgd']:,.2f}")
    print(f"Illustrative FX revenue (SGD): {metrics['total_fx_revenue_sgd']:,.2f}")
    print(f"Average ticket (SGD): {metrics['avg_ticket_sgd']:,.2f}")
    print(f"Average FX revenue per transaction (SGD): {metrics['avg_fx_revenue_per_txn_sgd']:,.2f}")
    print(f"Large payment flag rate: {metrics['large_payment_flag_rate']:.1%}")
    print("\nTop FX revenue corridors (SGD):")
    print(metrics["corridor_revenue_sgd"].head().to_string())

    if args.plot and not df.empty:
        plot_dashboard(df, metrics["corridor_revenue_sgd"])


if __name__ == "__main__":
    main()
