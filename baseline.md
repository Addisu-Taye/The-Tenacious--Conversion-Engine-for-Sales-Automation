# τ²-Bench Baseline (Interim)

## What was reproduced

A retail-domain smoke test using τ²-Bench was executed using:

- Domain: retail
- Tasks: 3 (smoke test)
- Trials: 1
- Model: gpt-4.1 (agent + user)

The system successfully initialized:
- domain registry
- agent and user simulators
- task execution pipeline

## Confidence interval

A full baseline with ≥50 tasks has not yet been executed.  
Therefore, no statistically valid 95% confidence interval is available at this stage.

## Cost per run

Approximate cost per smoke test run is low due to:
- small number of tasks (3)
- limited steps per task

Exact cost tracking will be implemented during Act I full evaluation runs.

## Unexpected behavior

- Windows encoding issue (`UnicodeEncodeError`) caused by Rich console rendering.
- Resolved by setting:
  ```powershell
  $env:PYTHONIOENCODING="utf-8"