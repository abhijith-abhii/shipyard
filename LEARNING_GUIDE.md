# Shipyard — learning guide

## What it does

Ship a health-checked service through CI. The intended user is junior platform engineers. Browser controls → validated Flask API → project analysis/workflow → results and export.

## Run and demonstrate

Follow the README installation block, then: Run docker compose up --build, open the app, fingerprint a payload and run python smoke.py. Inspect the verified GitHub Actions run for build, non-root and smoke evidence.

## Important files

- `app.py` — local HTTP interface and request/error handling.
- `core.py` — project-specific logic.
- `tests/` — regression and correctness checks.
- `reports/` — recorded outputs and verification evidence.

## Three engineering decisions

1. Package a deterministic API with a non-root runtime and read-only container filesystem.
2. CI runs unit tests before building, then starts a real temporary container and checks readiness plus a known digest.
3. Keep rollback instructions explicit and retain prior image tags rather than assuming deployment success.

## Five interview questions

1. **What does the delivery pipeline deploy?** It builds the project image and launches a temporary container inside the CI runner. The container is removed afterward; this is not a continuously hosted public service.

2. **How is the runtime constrained?** The image uses a non-root user. The run drops Linux capabilities, makes the root filesystem read-only and grants a temporary writable directory only where needed.

3. **What do smoke checks prove?** The service responds to its health endpoint and its main fingerprint workflow. This verifies basic operation of the built image, not sustained capacity or production reliability.

4. **Why identify images by commit?** A commit-specific tag connects the tested application to its source revision. A mutable latest tag would make reproducing a particular release more ambiguous.

5. **What is the rollback limitation?** The documented process can select a prior image, but there is no production orchestrator or live traffic cutover in this project. No zero-downtime rollback claim is made.

## Independent exercise

Add a readiness dependency that can intentionally fail, and prove the pipeline blocks promotion.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Delivered a non-root containerized service through GitHub Actions, with a read-only runtime, health and functional smoke checks, and captured temporary-deployment evidence.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
