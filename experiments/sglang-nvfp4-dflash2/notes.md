# Notes

The launcher assembled some arguments twice. [config/as-run.json](config/as-run.json) keeps the inspected argument array verbatim and lists the last-value-wins settings separately. The effective configuration used DFlash2 with eight draft tokens, unquantized BF16 draft weights, FP8 E4M3 KV cache, a 0.80 static memory fraction, and tensor parallel size 1 (the single GB10 GPU).

The 34.18 tok/s result is a controlled sequential mean. No matching controlled C2 or C4 cohort was run, so it cannot support a concurrency comparison with vLLM. The large server-log sample in [results/server-log-summary.json](results/server-log-summary.json) is retained only as organic telemetry.

The launcher forwarded `HF_TOKEN` when available. Its value was deliberately excluded from this repository.
