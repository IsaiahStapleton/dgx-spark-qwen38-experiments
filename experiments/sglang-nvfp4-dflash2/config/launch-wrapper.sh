#!/usr/bin/env bash
set -euo pipefail

QWEN_LAUNCHER_DIR=${QWEN_LAUNCHER_DIR:-Qwen3.8-27B-SGLang-DGX-Spark}

if [[ ! -d "${QWEN_LAUNCHER_DIR}/.git" ]]; then
  git clone https://github.com/MiaAI-Lab/Qwen3.8-27B-SGLang-DGX-Spark.git "${QWEN_LAUNCHER_DIR}"
fi

git -C "${QWEN_LAUNCHER_DIR}" checkout 751e29eb6a3057ccfd8f992f87dfc260787e05a1
cd "${QWEN_LAUNCHER_DIR}"

export IMAGE=lmsysorg/sglang:dev-qwen38-27b-dflash2
export MAX_CONCURRENT_REQUESTS=8
export CHUNKED_PREFILL=2048
export DF_EXTRA="--mem-fraction-static 0.80 --disable-flashinfer-autotune --cuda-graph-max-bs-decode 8 --enable-torch-compile --torch-compile-max-bs 4 --num-continuous-decode-steps 2 --sleep-on-idle --speculative-draft-model-quantization unquant --max-mamba-cache-size 40 --host 127.0.0.1"

./start-dflash.sh
