"""Small, dependency-free helpers for the published result tables.

The public kit deliberately keeps this module boring. It parses CSV files,
checks required fields and computes transparent mean/std summaries. It does
not download data, launch training or infer missing measurements.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple


@dataclass(frozen=True)
class ExperimentRow:
    """One row from ``results/metrics.csv``.

    Optional secondary measurements remain ``None`` when the source CSV cell
    is blank. Treating missing data as missing rather than zero prevents silent
    distortion of the reported summaries.
    """

    experiment: str
    seed: int
    model: str
    parameters: int
    train_tokens: int
    val_loss: float
    perplexity: Optional[float]
    flops_per_token_m: Optional[float]
    tokens_per_second: Optional[float]
    memory_peak_gb: Optional[float]
    status: str


def _optional_float(value: str) -> Optional[float]:
    return None if value == "" else float(value)


def load_metrics(path: Path) -> List[ExperimentRow]:
    """Load and validate the primary metrics CSV."""

    required = {
        "experiment", "seed", "model", "parameters", "train_tokens",
        "val_loss", "perplexity", "flops_per_token_m", "tokens_per_second",
        "memory_peak_gb", "status",
    }
    rows: List[ExperimentRow] = []
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        if reader.fieldnames is None or set(reader.fieldnames) != required:
            raise ValueError("metrics.csv has an unexpected header")
        for raw in reader:
            rows.append(ExperimentRow(
                experiment=raw["experiment"],
                seed=int(raw["seed"]),
                model=raw["model"],
                parameters=int(raw["parameters"]),
                train_tokens=int(raw["train_tokens"]),
                val_loss=float(raw["val_loss"]),
                perplexity=_optional_float(raw["perplexity"]),
                flops_per_token_m=_optional_float(raw["flops_per_token_m"]),
                tokens_per_second=_optional_float(raw["tokens_per_second"]),
                memory_peak_gb=_optional_float(raw["memory_peak_gb"]),
                status=raw["status"],
            ))
    return rows


def summarize_loss(rows: Iterable[ExperimentRow]) -> Dict[Tuple[str, str], Tuple[float, float, int]]:
    """Return ``(mean, sample_std, count)`` grouped by experiment/model.

    The published multi-seed table uses the sample standard deviation. A
    one-row group has no dispersion estimate, so its standard deviation is
    reported as ``0.0`` for a stable machine-readable output.
    """

    grouped: Dict[Tuple[str, str], List[float]] = {}
    for row in rows:
        grouped.setdefault((row.experiment, row.model), []).append(row.val_loss)

    summary: Dict[Tuple[str, str], Tuple[float, float, int]] = {}
    for key, values in grouped.items():
        mean = sum(values) / len(values)
        variance = (
            sum((value - mean) ** 2 for value in values) / (len(values) - 1)
            if len(values) > 1 else 0.0
        )
        summary[key] = (mean, math.sqrt(variance), len(values))
    return summary
