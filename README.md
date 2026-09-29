# Cross-Border Payments Analytics

A small Python learning project that generates synthetic cross-border payments and explores FX conversion and basic transaction metrics. All rates and transactions are illustrative; this is not a production payment system or a model of any company's pricing.

## How one transaction works

```text
Source amount (e.g. 100 SGD)
  → illustrative mid-market rate (3.4 MYR/SGD)
  → customer rate after 1% markup (3.366 MYR/SGD)
  → recipient gets 336.60 MYR
  → illustrative provider FX revenue = 1 SGD
```

The markup is modeled as a reduction in the target currency paid out. The resulting FX revenue is an illustrative SGD equivalent of the difference from the mid-market payout. It excludes transaction fees, processing costs, liquidity costs, taxes, and profit.

## What the code does

- `src/simulation.py`: generates reproducible synthetic transactions with a local random generator; converts source amounts to SGD using fixed assumptions; calculates mid-market and customer rates, recipient payout, and illustrative FX revenue.
- `src/risk_model.py`: labels payments above SGD 1,500 as large. This flag is **not** a fraud or risk score.
- `src/metrics.py`: adds SGD-normalized payment volume and revenue, computes averages, the large-payment flag rate, and FX revenue by currency corridor.
- `main.py`: prints a summary and optionally displays two charts.

Fixed assumptions in the code: SGD per source unit = SGD 1, USD 1.35, EUR 1.47; target units per SGD = THB 26, MYR 3.4, IDR 11,500. These are teaching inputs, not live FX quotes. The simulated customer rate is the mid-market rate multiplied by `1 - markup_percent / 100`.

## Run

```bash
python -m pip install -r requirements.txt
python main.py
python main.py --plot
```

Use `python main.py --transactions 0` to check the empty-data case. The charts require a graphical environment. The simulation is deterministic by default (seed 42); rates remain fixed across the simulated dates.

## Limits

There is no external transaction feed, historical rate data, database, payment API, transaction fee, processing cost, gross margin, or fraud detection. The model illustrates concepts and should not be used for pricing or financial decisions.
