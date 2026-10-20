# Day 1 — Safe Local Cybersecurity Lab

This project verifies the local environment and creates a safe portfolio workspace. It performs local tool/version checks only; it does not scan hosts, send network requests, test third-party systems, or change Windows settings.

## Run

```powershell
python .\src\verify_environment.py
python -m unittest discover -s .\tests -v
```

## Acceptance criteria

- Python is available and the verifier runs.
- Portfolio directories exist.
- Evidence is saved as `evidence/environment-check.json`.
- Tests pass.
- Network testing remains explicitly marked NOT RUN.