# Scripts

Run from this repository's root.

```bash
# Point this at an SSH tunnel or run it on the Spark host.
python3 scripts/benchmark.py --base-url http://127.0.0.1:8888/v1

# Reproduce the throughput experiment's sequential prompt exactly.
python3 scripts/benchmark.py --label-sequential --output benchmark.local.json

python3 scripts/validate_results.py
```

`collect-environment.sh` prints a read-only host/runtime inventory. Launch scripts live with their experiments because their mounts and engine flags differ.
