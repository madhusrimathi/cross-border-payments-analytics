from src.simulation import generate_transactions
from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring

import matplotlib.pyplot as plt


def plot_corridors(corridor_revenue):
    ax = corridor_revenue.head(5).plot(kind="bar")
    ax.set_title("Top Revenue Corridors")
    ax.set_ylabel("Revenue")
    ax.set_xlabel("Corridor")
    plt.xticks(rotation=30, ha="right")
    plt.tight_layout()
    plt.show()

def plot_daily_revenue(df): 
    daily = df.set_index("timestamp")["revenue"].resample("D").sum()
    daily.plot()
    plt.title("Daily Revenue Trend")
    plt.ylabel("Revenue")
    plt.xlabel("Date")
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

    plot_corridors(metrics["corridor_revenue"])
    plot_daily_revenue(df)


    


if __name__ == "__main__":
    main()
