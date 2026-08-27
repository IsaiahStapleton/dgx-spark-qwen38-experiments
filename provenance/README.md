# Provenance

The repository was assembled from live container inspection, server startup logs, benchmark command output, Hugging Face cache metadata, and host inventory on `dgx-spark-4`.

Each `benchmark.json` lists the ordinal of the original local Codex session event containing the command and raw output. The complete session was not copied because it also contains unrelated operational context. Exact measured output is transcribed into the result files; exact inspected launch arguments are in each `config/as-run.json`.

Sensitive values, especially `HF_TOKEN`, were not retained. No benchmark result or configuration value was inferred when an artifact was absent; missing SGLang concurrency data is explicitly represented as `null`.
