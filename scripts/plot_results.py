#!/usr/bin/env python3
"""Create simple, presentation-ready plots from the public CSV table.

Matplotlib is an optional dependency. The script intentionally plots only
measurements present in the CSV and never fabricates missing seed values.
"""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from gdn2_scaling.metrics import load_metrics, summarize_loss  # noqa: E402


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    try:
        import matplotlib.pyplot as plt
    except ImportError as exc:
        raise SystemExit("Install matplotlib with: pip install -e '.[plots]'") from exc

    rows = load_metrics(ROOT / "results" / "metrics.csv")
    summary = summarize_loss(rows)
    args.output_dir.mkdir(parents=True, exist_ok=True)

    labels, means, errors = [], [], []
    for key in (("30m", "gdn2_flat"), ("30m", "transformer"),
                ("120m", "gdn2_flat"), ("120m", "transformer")):
        mean, std, _ = summary[key]
        labels.append(f"{key[0]}\n{key[1]}")
        means.append(mean)
        errors.append(std)

    figure, axis = plt.subplots(figsize=(8, 4.5))
    axis.bar(labels, means, yerr=errors, capsize=4, color=["#91b7ff", "#d9d9d9"] * 2)
    axis.set_ylabel("Validation loss (nats)")
    axis.set_title("GDN2 vs Transformer: validation loss")
    axis.grid(axis="y", alpha=0.2)
    figure.tight_layout()
    figure.savefig(args.output_dir / "validation-loss.png", dpi=180)
    print(args.output_dir / "validation-loss.png")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
