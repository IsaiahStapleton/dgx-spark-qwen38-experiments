#!/usr/bin/env python3
"""Check recorded arithmetic and required result fields."""

import json
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def close(actual, expected, tolerance=0.02):
    return math.isclose(actual, expected, abs_tol=tolerance)


def main():
    files = sorted((ROOT / "experiments").glob("*/results/benchmark.json"))
    if not files:
        raise SystemExit("no benchmark result files found")

    summaries = {}
    for path in files:
        data = json.loads(path.read_text())
        sequential = data["measurements"]["sequential"]
        mean = sum(row["tokens_per_second"] for row in sequential) / len(sequential)
        expected_mean = data["summary"]["sequential_mean_tokens_per_second"]
        if not close(mean, expected_mean):
            raise SystemExit(f"{path}: sequential mean mismatch")

        for row in [data["measurements"]["warmup"], *sequential]:
            computed = row["completion_tokens"] / row["elapsed_seconds"]
            if not close(computed, row["tokens_per_second"]):
                raise SystemExit(f"{path}: request rate mismatch")

        for cohort in data["measurements"].get("concurrent", {}).values():
            computed = sum(row["completion_tokens"] for row in cohort["requests"])
            computed /= cohort["wall_seconds"]
            if not close(computed, cohort["aggregate_tokens_per_second"]):
                raise SystemExit(f"{path}: cohort aggregate mismatch")

        summaries[data["experiment"]] = data["summary"]
        print(f"ok: {path.relative_to(ROOT)}")

    comparison = json.loads((ROOT / "comparison.json").read_text())
    for row in comparison["experiments"]:
        summary = summaries[row["id"]]
        expected = {
            "sequential_mean": summary["sequential_mean_tokens_per_second"],
            "c2_aggregate": summary["c2_aggregate_tokens_per_second"],
            "c4_aggregate": summary["c4_aggregate_tokens_per_second"],
        }
        for key, value in expected.items():
            if value is None and row[key] is None:
                continue
            if not close(row[key], value):
                raise SystemExit(f"comparison.json: {row['id']} {key} mismatch")
    print("ok: comparison.json")


if __name__ == "__main__":
    main()
