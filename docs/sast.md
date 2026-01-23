# SAST + SCA Runbook (Snyk)

This document covers the detailed workflow for running **Snyk Code (SAST)** and
**Snyk Open Source (SCA)** in this repo. Snyk Open Source focuses on source
dependency manifests and transitive packages (not the container image). The
workflow is **manual-only** and intended for demos.

## Pipeline overview

1. Scope and guardrails (threshold, scan path, exclusions)
2. Run Snyk Code (SAST) and generate SARIF + JSON
3. Run Snyk Open Source (SCA) and generate SARIF + JSON
4. Upload SARIF to GitHub Code Scanning (separate categories)
5. Upload artifacts with timestamped names for auditing

## How to run

1. Go to **Actions** → **SAST (Snyk Code)** → **Run workflow**.
2. Pick:
   - `severity-threshold` (low/medium/high)
   - `scan-path` (default: `Controllers`)
   - `exclude` (default: `wwwroot,Database,bin,obj`)
3. Wait for the workflow to complete.

## Required secrets

- `SNYK_TOKEN` (required): Create in https://app.snyk.io and add to GitHub
  Actions secrets.
- `SNYK_ORG` (optional): Pin scans to a specific Snyk org ID.

## Prerequisites

- Enable **Snyk Code** for your org after creating the token (Snyk UI:
  Settings/Products -> Snyk Code).

## Outputs

Reports are generated under `reports/` during the run:

- `reports/snyk-code.sarif` (SAST SARIF)
- `reports/snyk-code.json` (SAST JSON)
- `reports/snyk-oss.sarif` (SCA SARIF)
- `reports/snyk-oss.json` (SCA JSON)

Artifacts are uploaded with timestamps:

- `snyk-sast-YYYYMMDD-HHMMSS`
- `snyk-sca-YYYYMMDD-HHMMSS`

## Where to view results

- **Security → Code scanning** in GitHub:
  - Category `snyk-code-sast` (SAST)
  - Category `snyk-oss-sca` (SCA)
- **Actions → Run → Artifacts** for raw SARIF/JSON downloads.

## Troubleshooting

- **Snyk Code not enabled** (`SNYK-CODE-0005`): Enable Snyk Code in org settings.
- **No findings in Code Scanning**: Check the branch filter in the Code Scanning UI.
- **Long SCA runs**: `--all-projects` resolves dependencies across the repo.

## Demo tips

- Use `scan-path=Controllers` for faster SAST demos.
- Keep `exclude` focused on static assets and generated output.
