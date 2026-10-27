# Git Bisect Demo

This repository demonstrates **batch CI for high-volume agent changes**.

Feature branches can contain any number of agent commits. Each is squash-merged to `dev`, producing one reviewable, atomic integration commit. Every push receives dependency-free fast checks. The full suite runs only when:

- the number of `dev` commits since `ci-last-green` reaches 100; or
- someone starts **Batch CI** manually from the GitHub Actions page.

If full CI fails, the workflow runs `git bisect run python scripts/full_test.py` between `ci-last-green` and the failed immutable `dev` SHA. Its job summary identifies the first bad squash-merge commit.

## Demo setup

`dev` begins at the `ci-last-green` tag. The twelve `feature/agent-*` branches are intentionally simple and are squash-merged into `dev`. `feature/agent-07` enables `broken_feature`, so a manual Batch CI run should find its squash merge as the first bad commit.

## Run locally

```powershell
python scripts/check_static.py
python scripts/full_test.py

# After the feature branches have been squash-merged to dev:
git bisect start <failed-dev-sha> ci-last-green
git bisect run python scripts/full_test.py
git bisect reset
```

Git considers a zero exit code good and a non-zero exit code bad. For a range of 100 feature commits, it needs about seven full-suite runs instead of 100.

## Production notes

The demo’s `full_test.py` is intentionally tiny. Replace it with your real integration suite; it must be deterministic for bisection to be trustworthy. Keep the tested range immutable: merges arriving while a failure is investigated belong to the next batch.
