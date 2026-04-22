# The Tenacious Conversion Engine

TRP1 Week 10 challenge project for Tenacious Consulting and Outsourcing.

## Overview

This project is an AI-assisted lead generation and conversion system designed around the Tenacious challenge specification. The current build establishes the Day 0 and early interim infrastructure needed for:

- outbound email delivery
- inbound SMS/webhook handling
- HubSpot CRM writes
- Langfuse observability
- public-signal scraping with Playwright
- τ²-Bench evaluation setup

## Architecture

```text
Signals -> Agent -> Channels -> Webhooks -> CRM -> Observability -> Evaluation
Components
Email: Resend
SMS: Africa's Talking sandbox
CRM: HubSpot Developer Sandbox
Observability: Langfuse
Webhooks/API: FastAPI + ngrok
Evaluation: τ²-Bench
Signal pipeline: Playwright
Current Status
Verified Running
Resend outbound email
Africa's Talking inbound SMS webhook
HubSpot contact creation/update
Langfuse trace submission
FastAPI webhook server via ngrok
Playwright public-page fetch
τ²-Bench retail smoke test setup
Partial / Pending
Cal.com local deployment
full enrichment pipeline
competitor gap pipeline
full τ²-Bench baseline scoring
p50/p95 latency across 20+ interactions
Repository Structure
agent/
  app.py
  email_handler.py
  hubspot_client.py
  observability/
    langfuse_client.py

scripts/
  test_langfuse.py
  test_hubspot.py
  test_resend.py
  test_email_flow.py
  test_signal_fetch.py

configs/
  enrichment_sample.json
  competitor_gap_brief.json
  seed_repo_check.md
  data_handling_ack.md

eval/
  tau2_smoke_output.txt
  tau2-bench/
Setup
1. Create environment
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
2. Configure environment variables

Create .env with:

LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=
LANGFUSE_BASE_URL=https://cloud.langfuse.com

HUBSPOT_ACCESS_TOKEN=

RESEND_API_KEY=
FROM_EMAIL=

AFRICASTALKING_USERNAME=sandbox
AFRICASTALKING_API_KEY=
AFRICASTALKING_SHORTCODE=
3. Start the API server
uvicorn agent.app:app --reload --port 8000
4. Expose webhook locally
ngrok http 8000
Smoke Tests
Langfuse
python -m scripts.test_langfuse
HubSpot
python -m scripts.test_hubspot
Email
python -m scripts.test_resend
Traced email flow
python -m scripts.test_email_flow
Playwright signal fetch
python -m scripts.test_signal_fetch
τ²-Bench

From eval/tau2-bench:

uv sync
$env:PYTHONIOENCODING="utf-8"
uv run tau2 run --domain retail --agent-llm gpt-4.1 --user-llm gpt-4.1 --num-trials 1 --num-tasks 3
Interim Notes

This repo currently demonstrates the infrastructure and prototype artifacts required for interim submission. Some challenge deliverables are represented as sample schemas or prototype outputs rather than full production implementations at this stage.

Data Handling
no real Tenacious customer data used
all current prospect records are synthetic/test records
Tenacious-branded outputs should be treated as draft artifacts

### Why this helps
This README makes the repo legible to graders in under 2 minutes.

---

## 4) Latency estimate

Since the rubric asks for **p50/p95 latency numbers from at least 20 real email and SMS interactions pulled from trace log**, the strict answer is:

- if you do **not** have 20 interactions yet, you should **not claim final latency metrics**
- but you can still add a **provisional latency note** and explain that the 20-interaction requirement is not yet fully satisfied

### Best honest path
Create:

```text
configs/latency_estimate.md

Use this:

# Latency Estimate (Interim)

## Status
This is a provisional latency note, not the final required benchmark.

The challenge asks for p50/p95 latency from at least 20 real email and SMS interactions pulled from the trace log. That interaction volume has not yet been reached in the current interim state.

## Current Observation
Based on the completed smoke tests and traced email flow, the system is already capturing per-interaction latency in Langfuse metadata.

## Planned Method
1. Execute at least 20 combined email and SMS interactions.
2. Export or inspect the trace metadata.
3. Extract `latency_ms` values.
4. Compute:
   - p50 latency
   - p95 latency

## Interim Placeholder
- p50 latency: pending sufficient sample size
- p95 latency: pending sufficient sample size

## Note
No final latency claim is made yet in order to avoid overstating current evidence.