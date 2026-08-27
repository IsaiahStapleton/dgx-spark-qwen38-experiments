# Notes

This was the first vLLM comparison. It used the FP8 checkpoint, FP8 KV cache, tensor parallel size 1, and three MTP speculative tokens. No explicit performance mode was supplied, so vLLM selected its default balanced mode and a 2,048-token scheduler budget.

Unlike the later NVFP4 tests, this container did not mount persistent vLLM or Triton compilation caches. Startup compile timings therefore should not be compared as serving throughput metrics.

The image and model revisions are recorded in [../../environment/artifacts.lock.json](../../environment/artifacts.lock.json).
