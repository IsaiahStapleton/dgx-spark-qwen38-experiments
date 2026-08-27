# Test environment

Collected from `dgx-spark-4` after the experiments.

| Component | Value |
|---|---|
| System | Lenovo ThinkStation PGX (DGX Spark-class) |
| GPU | NVIDIA GB10 |
| Architecture | aarch64 |
| CPU | 20 cores: 10 Cortex-X925 + 10 Cortex-A725 |
| Unified memory | 128,452,669,440 bytes (119.63 GiB) |
| OS | Ubuntu 24.04.4 LTS |
| Kernel | 6.17.0-1014-nvidia |
| NVIDIA driver | 580.142 |
| Docker server | 29.2.1 |
| CUDA reported by PyTorch | 13.0 |

The active endpoint was bound to `127.0.0.1:8888` on the Spark host. Tests reached it through an SSH tunnel; it was not exposed on all host interfaces.
