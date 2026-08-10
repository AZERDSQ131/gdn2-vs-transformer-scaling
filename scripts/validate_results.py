#!/usr/bin/env python3
"""Validate the public result tables and print reproducible summaries."""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gdn2_scaling.metrics import load_metrics, summarize_loss  # noqa: E402


def main() -> int:
    rows = load_metrics(ROOT / "results" / "metrics.csv")
    if len(rows) != 8:
        raise SystemExit(f"expected 8 primary rows, found {len(rows)}")

    experiments = {row.experiment for row in rows}
    if experiments != {"30m", "120m"}:
        raise SystemExit(f"unexpected experiments: {sorted(experiments)}")

    summary = summarize_loss(rows)
    print("experiment,model,mean_val_loss,population_std,count")
    for (experiment, model), (mean, std, count) in sorted(summary.items()):
        print(f"{experiment},{model},{mean:.4f},{std:.4f},{count}")

    provisional = [row for row in rows if row.experiment == "120m"]
    if any(row.status != "provisional" for row in provisional):
        raise SystemExit("120m rows must remain marked provisional")
    if len({row.seed for row in provisional}) != 1:
        raise SystemExit("the current 120m table should contain one seed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
