#!/usr/bin/env bash
set -euo pipefail

QWEN_HF_CACHE=${QWEN_HF_CACHE:-/home/redhat-et/Qwen3.8-27B-SGLang-DGX-Spark/.cache/huggingface}
QWEN_VLLM_CACHE=${QWEN_VLLM_CACHE:-/home/redhat-et/Qwen3.8-27B-vLLM-DGX-Spark/.cache/vllm}
QWEN_TRITON_CACHE=${QWEN_TRITON_CACHE:-/home/redhat-et/Qwen3.8-27B-vLLM-DGX-Spark/.cache/triton}
QWEN_IMAGE=${QWEN_IMAGE:-vllm/vllm-openai:qwen38}

docker run -d \
  --name qwen3.8-27b-vllm-nvfp4-test \
  --gpus all \
  --ipc=host \
  -p 127.0.0.1:8888:8888 \
  -v "${QWEN_HF_CACHE}:/root/.cache/huggingface" \
  -v "${QWEN_VLLM_CACHE}:/root/.cache/vllm" \
  -v "${QWEN_TRITON_CACHE}:/root/.triton" \
  "${QWEN_IMAGE}" \
  Inferact/Qwen3.8-27B-NVFP4 \
  --served-model-name qwen3.8-27b-sglang \
  --host 0.0.0.0 \
  --port 8888 \
  --tensor-parallel-size 1 \
  --gpu-memory-utilization 0.80 \
  --max-model-len 262144 \
  --kv-cache-dtype fp8 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
