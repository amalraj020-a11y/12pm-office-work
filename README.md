# Amala Cyber Guardian

Daily autonomous cybersecurity research portfolio.

## Daily 12:00 PM IST run

Amala starts at 12:00 PM India Standard Time and performs an authorization-first, low-impact research session:

1. Selects organizations worldwide across technology, entertainment, media, consumer goods, e-commerce, education, and open source.
2. Checks official vulnerability disclosure or bug bounty rules before any testing.
3. Performs only passive public checks unless explicit authorization is verified.
4. Uses free local tools and Ollama models, with Qwen3:4B preferred.
5. Reviews results for false positives, duplicates, confidence, and severity.
6. Saves a dated Markdown report and supporting evidence.
7. Updates the daily folder and pushes the report to this GitHub repository.
8. Never exploits systems, accesses private data, submits reports, emails security teams, or contacts employees without Raj's approval.

If the local model is slow or unavailable, the runner records the limitation and still saves a safe report instead of claiming a vulnerability.

## Folder structure

- `amala-cybersecurity/Day-01/` - completed lab setup, tests, and safe curl evidence.
- `amala-cybersecurity/Day-02/` - next planned Python security toolkit work.
- `reports/cyber-guardian/` - dated daily run reports.
- `automation/` - the Windows scheduled runner and launcher.

## Safety status

This project is for responsible security research only. No finding is treated as confirmed without evidence and verified authorization. External disclosure always requires Raj's approval.