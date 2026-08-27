# Notes

This test added `--performance-mode throughput` to the NVFP4 balanced configuration. The effective scheduler budget increased from 2,048 to 4,096 batched tokens, producing the best vLLM result at each tested load.

After validation, the test container was retained as `qwen3.8-27b-vllm` with restart policy `unless-stopped`. The served model alias intentionally remains `qwen3.8-27b-sglang` for client compatibility even though the runtime is vLLM.

The post-test MTP counter was 3,077 accepted tokens out of 3,597 drafts (85.54%); it includes benchmark and validation traffic and is not an isolated benchmark metric.
