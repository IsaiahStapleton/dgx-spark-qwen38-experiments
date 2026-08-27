# Qwen3.8-27B on DGX Spark

Four Qwen3.8-27B serving configurations were tested on one NVIDIA DGX Spark-class system (Lenovo ThinkStation PGX, GB10, 128 GB unified memory, Ubuntu 24.04, CUDA 13.0).

| Configuration | Single request | C2 aggregate | C4 aggregate | Detail |
|---|---:|---:|---:|---|
| SGLang NVFP4 + DFlash2 | **34.18 tok/s** | — | — | [experiment](experiments/sglang-nvfp4-dflash2/) |
| vLLM FP8 + MTP3, balanced | 18.87 tok/s | 38.82 tok/s | 64.59 tok/s | [experiment](experiments/vllm-fp8-mtp-balanced/) |
| vLLM NVFP4 + MTP3, balanced | 19.52 tok/s | 37.54 tok/s | 70.46 tok/s | [experiment](experiments/vllm-nvfp4-mtp-balanced/) |
| vLLM NVFP4 + MTP3, throughput | **22.30 tok/s** | **45.32 tok/s** | **79.40 tok/s** | [experiment](experiments/vllm-nvfp4-mtp-throughput/) |

## Conclusions

- SGLang was fastest in the controlled single-request test; no equivalent controlled concurrency result was collected for it.
- NVFP4 reduced vLLM's loaded model footprint from 28.95 GiB to 24.97 GiB.
- vLLM throughput mode was the best vLLM configuration at single-request, C2, and C4 load and is the retained deployment.
- C2/C4 values are one cohort each, so treat them as directional rather than statistically rigorous.

See [methodology.md](methodology.md), [environment/](environment/), and [scripts/](scripts/) for reproduction details.
