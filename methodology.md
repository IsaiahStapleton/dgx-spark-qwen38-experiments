# Benchmark methodology

## Controlled benchmark

The benchmark used Python's standard-library HTTP client against the OpenAI-compatible `/v1/completions` endpoint through a local SSH tunnel to Spark port 8888.

- Model alias: `qwen3.8-27b-sglang` (the legacy alias was retained after switching runtimes)
- Sampling: temperature 0, `ignore_eos=true`
- Workload: fixed integer-continuation prompt
- Warmup: one 32-token request, discarded
- Sequential: two 512-token requests; reported value is their arithmetic mean
- Concurrent: one cohort of two and one cohort of four 512-token requests
- Per-request rate: `completion_tokens / request wall time`
- Aggregate rate: total completion tokens divided by cohort wall time

The committed [benchmark.py](scripts/benchmark.py) reproduces the methodology. Each result file also records the exact prompt variant used in that run.

## Limitations

- C2 and C4 each contain one cohort, without repeated trials or confidence intervals.
- No controlled C2/C4 benchmark was collected for the SGLang configuration.
- Client timing includes time to first token and SSH/network overhead.
- Background load was not explicitly isolated.
- The throughput-mode sequential prompt included the suffix `(stream single)`; the other sequential tests did not.
- Historical SGLang server-log telemetry is kept separately from controlled results because it represents mixed organic traffic.
