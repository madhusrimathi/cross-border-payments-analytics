from src.simulation import generate_transactions
from src.metrics import compute_metrics
from src.risk_model import apply_risk_scoring

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

if __name__ == "__main__":
    main()
