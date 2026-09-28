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

1. **What problem does this project solve, and what is its unit of work?** Explain ship a health-checked service through ci, identify junior platform engineers as the audience, and trace one concrete example through the files above. Use the demonstration output rather than hypothetical impact.
2. **Why did you choose the first design decision?** Package a deterministic API with a non-root runtime and read-only container filesystem. Show the corresponding implementation and a test that would fail if that property were removed.
3. **How do you protect correctness when inputs or execution change?** CI runs unit tests before building, then starts a real temporary container and checks readiness plus a known digest. Explain the relevant invalid-input or edge-case test and distinguish a checked property from an untested assumption.
4. **How do you make results inspectable and reproducible?** Keep rollback instructions explicit and retain prior image tags rather than assuming deployment success. Point to actual outputs and recorded commands. Explain why a successful example is weaker evidence than a tested boundary or independently reconciled total.
5. **What would you improve before real deployment or real-data use?** The delivery target is an ephemeral CI container or local Docker Compose. No public service, registry publishing, TLS, zero-downtime rollout or production traffic is configured. Docker image base tags are versioned but not digest-pinned. Choose one limitation, describe the missing evidence, and propose a measurable acceptance check rather than promising production readiness.

## Independent exercise

Add a readiness dependency that can intentionally fail, and prove the pipeline blocks promotion.

Write down the expected behavior before editing. Add a meaningful regression check, run the existing suite, and describe what changed in your own words.

## Contribution and resume guidance

The implementation was developed with substantial AI assistance under Abhijith Viswanathan's direction. The verified contribution is the working artifact and the learning work actually completed, not invented employment or adoption.

Suggested factual bullet after personally validating the demo:

- Implemented and validated ship a health-checked service through ci using Docker · GitHub Actions · Flask, with container build and documented correctness checks and limitations.

Use [VERIFICATION.md](VERIFICATION.md) to add only measured numbers. Do not claim production traffic, users, savings, upstream acceptance or cloud deployment without corresponding evidence.
