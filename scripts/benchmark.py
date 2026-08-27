#!/usr/bin/env python3
"""Run the controlled OpenAI-compatible completion benchmark used in this repo."""

import argparse
import concurrent.futures
import json
import os
import time
import urllib.request
from datetime import datetime, timezone


PROMPT = "Continue this sequence with only space-separated integers"
SEQUENCE = "1 2 3 4 5 6 7 8 9 10"


def request(url, model, stream_label, tokens, timeout):
    label = f" (stream {stream_label})" if stream_label is not None else ""
    payload = {
        "model": model,
        "prompt": f"{PROMPT}{label}: {SEQUENCE}",
        "temperature": 0,
        "max_tokens": tokens,
        "ignore_eos": True,
    }
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode(),
        headers={"Content-Type": "application/json"},
    )
    started = time.perf_counter()
    with urllib.request.urlopen(req, timeout=timeout) as response:
        body = json.load(response)
    elapsed = time.perf_counter() - started
    count = body["usage"]["completion_tokens"]
    return {
        "completion_tokens": count,
        "elapsed_seconds": round(elapsed, 3),
        "tokens_per_second": round(count / elapsed, 2),
        "finish_reason": body["choices"][0].get("finish_reason"),
    }


def cohort(url, model, concurrency, tokens, timeout):
    started = time.perf_counter()
    with concurrent.futures.ThreadPoolExecutor(max_workers=concurrency) as pool:
        results = list(
            pool.map(
                lambda i: request(url, model, i, tokens, timeout),
                range(concurrency),
            )
        )
    wall = time.perf_counter() - started
    return {
        "concurrency": concurrency,
        "requests": results,
        "wall_seconds": round(wall, 3),
        "aggregate_tokens_per_second": round(
            sum(item["completion_tokens"] for item in results) / wall, 2
        ),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--base-url",
        default=os.environ.get("QWEN_BASE_URL", "http://127.0.0.1:8888/v1"),
    )
    parser.add_argument("--model", default="qwen3.8-27b-sglang")
    parser.add_argument("--timeout", type=int, default=180)
    parser.add_argument("--output", help="Write the JSON result to this path")
    parser.add_argument(
        "--label-sequential",
        action="store_true",
        help="Use the '(stream single)' prompt from the throughput-mode run",
    )
    args = parser.parse_args()
    url = f"{args.base_url.rstrip('/')}/completions"
    sequential_label = "single" if args.label_sequential else None

    warmup = request(url, args.model, sequential_label, 32, args.timeout)
    sequential = [
        request(url, args.model, sequential_label, 512, args.timeout),
        request(url, args.model, sequential_label, 512, args.timeout),
    ]
    output = {
        "schema_version": 1,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "endpoint": url,
        "model": args.model,
        "sampling": {"temperature": 0, "ignore_eos": True},
        "sequential_prompt": f"{PROMPT}"
        + (" (stream single)" if args.label_sequential else "")
        + f": {SEQUENCE}",
        "concurrent_prompt_template": f"{PROMPT} (stream <index>): {SEQUENCE}",
        "warmup": warmup,
        "sequential": sequential,
        "concurrent": {
            "2": cohort(url, args.model, 2, 512, args.timeout),
            "4": cohort(url, args.model, 4, 512, args.timeout),
        },
        "summary": {
            "sequential_mean_tokens_per_second": round(
                sum(item["tokens_per_second"] for item in sequential)
                / len(sequential),
                3,
            )
        },
    }
    rendered = json.dumps(output, indent=2) + "\n"
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(rendered)
    print(rendered, end="")


if __name__ == "__main__":
    main()
