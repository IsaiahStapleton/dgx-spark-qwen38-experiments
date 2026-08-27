#!/usr/bin/env bash
set -euo pipefail

uname -a
cat /etc/os-release
lscpu
free -b
nvidia-smi
docker version
