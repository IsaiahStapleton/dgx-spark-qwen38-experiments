# vLLM FP8 + MTP3, balanced

- Target: `Qwen/Qwen3.8-27B-FP8`
- vLLM performance mode: default (`balanced`)
- Context: 262,144 tokens
- Controlled result: 18.87 tok/s sequential mean; 38.82 tok/s C2; 64.59 tok/s C4

See [config/as-run.json](config/as-run.json), [config/launch.sh](config/launch.sh), [results/benchmark.json](results/benchmark.json), and [notes.md](notes.md).
