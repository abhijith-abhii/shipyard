# Local rollout and rollback

Build a candidate with a distinct image tag, launch on port 8081, and run `python smoke.py http://127.0.0.1:8081`. Keep the previous image tag until verification completes. To switch, stop the old named container and start the candidate on 8080. If smoke checks fail, restart the previous image tag on 8080 and rerun the checks.

The CI workflow builds and deploys a real container on an ephemeral GitHub runner, then removes it. It does not deploy a public service or claim zero-downtime rollout. It does not push an image to a registry.
