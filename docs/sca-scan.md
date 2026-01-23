# SCAScan Runbook (Trivy SBOM)

This document covers the workflow for running **SCAScan (Trivy SBOM)** against the Docker
image built from this repo. It scans OS packages and bundled runtime dependencies
that may not be visible in source manifests. The workflow is **workflow_dispatch**
only and does not run automatically.

## Pipeline overview

1. Build the Docker image
2. Generate a CycloneDX SBOM JSON
3. Scan the image for HIGH/CRITICAL vulnerabilities
4. Upload SBOM + summary artifacts
5. Fail the workflow on HIGH/CRITICAL findings

## How to run

1. Go to **Actions** → **SCAScan** → **Run workflow**
2. Pick:
   - `severity-threshold` (high/critical)
   - `image-tag` (default: `aspgoat-sca`)
3. Wait for the workflow to complete.

## Outputs

Reports are generated under `reports/` during the run:

- `reports/trivy-sbom.json` (CycloneDX JSON)
- `reports/trivy-critical.txt` (HIGH/CRITICAL summary)

Artifacts are uploaded with timestamps:

- `trivy-sca-YYYYMMDD-HHMMSS`

## Ignore rules

Trivy honors `.trivyignore` when present. Add one CVE per line to suppress
known demo findings.
