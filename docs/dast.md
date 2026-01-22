# DAST Runbook (OWASP ZAP Full Scan)

This document covers the workflow for running **OWASP ZAP Full Scan** as a
manual, demo-friendly DAST pipeline. The workflow is **workflow_dispatch**
only and does not run automatically.

## Pipeline overview

1. Decide scan inputs (threshold, LLM coverage)
2. Build and run the app in Docker
3. Login and capture an auth cookie
4. Run ZAP full scan (spider + AJAX spider + active scan)
5. Upload HTML/JSON reports as artifacts
6. Summarize results in the job summary (non-blocking)

## How to run

1. Go to **Actions** → **DAST (ZAP Full Scan)** → **Run workflow**
2. Pick:
   - `fail-threshold` (high/critical)
   - `include-llm` (true/false)
3. Wait for the workflow to complete.

## LLM coverage

If `include-llm=true`, the workflow first checks whether Ollama is reachable at
`http://localhost:11434`. If it is not reachable, LLM routes are skipped and
the summary calls this out.

LLM labs are gated by the `enableLlmLabs` config key. The workflow toggles this
value automatically when it runs the app container.

## Outputs

Reports are generated under `reports/` during the run:

- `reports/zap-report.html`
- `reports/zap-report.json`

Artifacts are uploaded with timestamped names:

- `zap-dast-YYYYMMDD-HHMMSS`

## Notes on severity

ZAP uses **High/Medium/Low/Info**. It does not have a native **Critical**
severity, so the `critical` threshold is treated as **High** for summary
purposes.

## Where to view results

- **Actions → Run → Summary** for the quick overview
- **Actions → Run → Artifacts** for the HTML/JSON report downloads
