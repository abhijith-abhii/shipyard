# Shipyard — verification

Verification date: 28 September 2026. Tests and examples were executed; they are not illustrative pass claims.

- Project checks: 9 passed.
- Dependency/setup verification: fresh isolated Python 3.12 environment passed.
- Main browser/API workflow: verified locally; actual result saved in reports/example-output.json.
- Publication: [public repository](https://github.com/abhijith-abhii/shipyard) verified under **abhijith-abhii**.
- Actual application screenshot: reports/screenshots/app.png. Browser rendered successfully at 1280px width.

## Verification boundaries
- Actual temporary CI container verified; no continuously hosted public service or production rollout.


## Evidence
- `reports/test-results.txt`: actual test output.
- `reports/clean-setup.json`: isolated setup result where applicable.
- `reports/publication-check.json`: credential-pattern and file audit.
- `DATA_AND_SOURCES.md`: source and license notes.

## GitHub verification

- [Container delivery: passed](https://github.com/abhijith-abhii/shipyard/actions/runs/36416088236)

Verified source revision: `ed0944c3839f5c11fc26cb82619b9fe558c46df9`. Subsequent presentation-only changes do not change that implementation evidence.
