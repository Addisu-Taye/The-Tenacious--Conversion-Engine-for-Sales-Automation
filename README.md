# The Tenacious Conversion Engine

TRP1 Week 10 Challenge — Addisu Taye

## Overview

This project implements an AI-assisted multi-channel conversion system designed to:

- Identify and engage prospects
- Conduct structured outreach
- Qualify leads
- Persist interactions in CRM
- Enable booking via Cal.com
- Provide observability and evaluation

The system is built incrementally following the challenge phases, with Day 0 and interim infrastructure fully established.

---

## Architecture

```mermaid
flowchart LR
    A[External Signals<br/>Playwright] --> B[Enrichment Layer]
    B --> C[Agent Layer]

    C --> D[Email Channel<br/>Resend]
    C --> E[SMS Channel<br/>Africa's Talking]

    D --> F[FastAPI Webhooks]
    E --> F

    F --> G[HubSpot CRM]
    F --> H[Langfuse Observability]

    G --> C

    C --> I[Cal.com Booking]

    C --> J[τ²-Bench Evaluation]
Production Stack
Component	Status
Resend (Email)	✅ Verified
Africa’s Talking (SMS)	✅ Verified
HubSpot Sandbox	✅ Verified
Langfuse	✅ Verified
Cal.com	✅ Verified (local + booking flow tested)
Repository Structure
agent/
  app.py
  email_handler.py
  hubspot_client.py
  calcom_client.py
  observability/

configs/
  enrichment_sample.json
  competitor_gap_brief.json
  seed_repo_check.md
  data_handling_ack.md

eval/
  score_log.json
  trace_log.jsonl

scripts/
  test_email_flow.py
  test_signal_fetch.py

baseline.md
README.md
Setup
1. Environment
python -m venv venv
venv\Scripts\activate
pip install -r agent/requirements.txt
2. Environment Variables

Create .env:

LANGFUSE_PUBLIC_KEY=
LANGFUSE_SECRET_KEY=

HUBSPOT_ACCESS_TOKEN=

RESEND_API_KEY=
FROM_EMAIL=

AFRICASTALKING_USERNAME=sandbox
AFRICASTALKING_API_KEY=

CALCOM_BASE_URL=http://localhost:3000
3. Run API
uvicorn agent.app:app --reload --port 8000
4. Expose Webhook
ngrok http 8000
Testing
Email Flow
python -m scripts.test_email_flow
Signal Fetch
python -m scripts.test_signal_fetch
Cal.com Setup
docker compose -f docker-compose.calcom.yml up -d

Then:

Create account
Create event type
Book test meeting
τ²-Bench
cd eval/tau2-bench
uv sync
$env:PYTHONIOENCODING="utf-8"
uv run tau2 run --domain retail --agent-llm gpt-4.1 --user-llm gpt-4.1 --num-trials 1 --num-tasks 3
Known Limitations (Interim)
Enrichment pipeline partially implemented
Competitor analysis is prototype
τ²-Bench full baseline pending
Latency metrics not yet at required scale
Data Handling
No real customer data used
All prospects are synthetic
Outputs treated as draft artifacts

---

# 📄 INTERIM SUBMISSION REPORT (DETAILED)

## TRP1 – The Tenacious Conversion Engine  
**Student:** Addisu Taye  

---

## 1. Architecture Overview & Design Decisions

The system follows a modular architecture:

### Layers

1. **Signal Layer**
   - Playwright scraping for job signals

2. **Enrichment Layer**
   - Prototype structure for firmographics and signals

3. **Agent Layer**
   - Central orchestration logic

4. **Channel Layer**
   - Email (Resend)
   - SMS (Africa’s Talking)

5. **Webhook Layer**
   - FastAPI endpoints for inbound communication

6. **CRM Layer**
   - HubSpot contact persistence

7. **Observability**
   - Langfuse tracing

8. **Booking**
   - Cal.com integration

9. **Evaluation**
   - τ²-Bench

---

## Key Design Decisions

- Email-first outreach model
- Modular integrations for isolation and debugging
- Observability-first instrumentation
- Synthetic data compliance
- Progressive system build (Day 0 → Act I → Act II)

---

## 2. Production Stack Status

| Component | Status |
|----------|--------|
| Resend | ✅ Working |
| Africa’s Talking | ✅ Working |
| HubSpot Sandbox | ✅ Working |
| Langfuse | ✅ Working |
| Cal.com | ✅ Working (Docker + booking verified) |

Evidence:
- Email sent successfully
- SMS webhook received
- HubSpot contact created
- Langfuse trace logged
- Cal.com booking completed

---

## 3. Enrichment Pipeline Status

| Component | Status |
|----------|--------|
| Job signal scraping | ✅ Partial (Playwright) |
| Firmographics | ⚠️ Prototype |
| layoffs.fyi | ❌ Not implemented |
| Leadership change | ❌ Not implemented |
| AI maturity score | ⚠️ Prototype |

Output artifact:
- `configs/enrichment_sample.json`

---

## 4. Competitor Gap Brief

Status: **Prototype implemented**

Output:
- `configs/competitor_gap_brief.json`

Includes:
- competitor identification
- gap hypotheses
- positioning strategy

---

## 5. τ²-Bench Baseline

### Methodology

- Domain: retail
- Tasks: 3
- Trials: 1
- Model: gpt-4.1

### Status

- Smoke test completed
- Full baseline pending

### Score

- Not computed yet (insufficient trials)

---

## 6. Latency Metrics

### Status

Not yet meeting requirement (20+ interactions)

### Current state

- Langfuse captures latency per interaction
- Aggregation not yet performed

### Plan

- Execute ≥20 interactions
- Extract metrics from trace logs
- compute p50 / p95

---

## 7. What Is Working

- Email delivery (Resend)
- SMS webhook (Africa’s Talking)
- FastAPI server
- ngrok routing
- HubSpot CRM integration
- Langfuse tracing
- Playwright signal extraction
- Cal.com booking flow
- τ²-Bench execution

---

## 8. What Is Not Working / Pending

- Full enrichment pipeline
- layoffs integration
- leadership detection
- AI maturity scoring (robust)
- τ²-Bench full evaluation
- latency aggregation

---

## 9. Plan for Remaining Days

### Act I
- Run full τ² baseline
- compute metrics

### Act II
- implement enrichment pipeline
- build scoring system
- integrate Cal.com deeply

### Act III
- optimize latency
- multi-channel orchestration

---

## 10. Conclusion

The system successfully establishes:

- complete production stack
- verified communication channels
- CRM persistence
- observability
- booking integration

The project is ready to transition into:
- evaluation optimization
- enrichment and conversion logic