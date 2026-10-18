# Local performance benchmark

Measured October 18, 2026 against application source `9a958a58d26ea49908fb62870420ec32ae1a0f07`. The benchmark files and documentation were added afterward; application code was unchanged.

## Workload and scope

POST /api/run SHA-256 fingerprints of 100000 ASCII characters; digest correctness checked. Native Gunicorn process, not a Docker benchmark.

Synthetic local loopback HTTP benchmark. Not production capacity, real users, clinical validation or user growth. These measurements describe one short workload on one machine. They do not establish a capacity ceiling, sustained service-level objective, p99 guarantee, production response time or adoption. No historical speedup is claimed unless a comparison is explicitly defined below.

Environment: Darwin 25.2.0, arm64, 12 logical CPUs, Python 3.12.14. Gunicorn 23.0.0, 1 gthread worker, 8 threads.

- 8 concurrent HTTP clients, 40 untimed warmup requests.
- 3 rounds of 800 measured requests: **2,400 total**.
- Requests use persistent local loopback HTTP connections. The client and server share one machine.
- Every response is checked for HTTP success and workload-specific correctness; failures abort without producing a successful report.
- All data is synthetic and isolated in a temporary directory.

## Results

| Round | Requests | Median latency | p95 latency | Requests/second | Failures |
|---|---:|---:|---:|---:|---:|
| 1 | 800 | 6.517 ms | 9.720 ms | 1160.77 | 0 |
| 2 | 800 | 6.352 ms | 9.743 ms | 1179.46 | 0 |
| 3 | 800 | 6.535 ms | 10.361 ms | 1148.02 | 0 |

Combined latency: **6.466 ms median**, **9.924 ms p95**. Median round throughput: **1160.77 requests/second**. All **2,400 requests passed** their checks. p95 is the nearest-rank 95th percentile; throughput includes client scheduling and validation.

This measures the service directly with Gunicorn and 100,000-byte input strings. It does not measure Docker image size, build acceleration, deployment time or cloud infrastructure.

## Reproduce

```sh
python3.12 -m venv .benchmark-venv
.benchmark-venv/bin/python -m pip install -r benchmarks/requirements.txt
.benchmark-venv/bin/python benchmarks/benchmark.py shipyard --output /tmp/shipyard-benchmark.json
```

Health Passport can select a Java executable with `--java /path/to/java`. Other benchmark modes need no Java. The script creates temporary data, starts only a loopback server and stops it after the run. Compare results only under controlled, comparable machine and workload conditions.

[Recorded JSON](results-2026-10-18.json) contains the source revision, environment, per-round results and comparison timings where applicable.
