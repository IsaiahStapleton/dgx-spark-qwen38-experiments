# Notes

This test changed the checkpoint from FP8 to NVFP4 while retaining vLLM's default balanced mode, FP8 KV cache, tensor parallel size 1, three MTP speculative tokens, and the full 262,144-token context.

The loaded model footprint fell from 28.95 GiB to 24.97 GiB. The post-test MTP counter was 2,859 accepted tokens out of 3,804 drafts (75.16%); this counter includes the benchmark workload and is not an isolated benchmark metric.
