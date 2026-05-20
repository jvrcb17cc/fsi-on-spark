# fsi-on-spark

A lightweight prototype for a modular, multi-agent financial analysis workflow.

## Overview

This project demonstrates a clean architecture for a local, CPU-friendly multi-agent system with deterministic mock data.

Key features:
- Modular agents with isolated `.run(input_dict)` interfaces
- Declarative orchestration pipeline
- Aggregation layer for normalized signal composition
- Execution trace / audit log for every agent step
- Simple schema layer using `TypedDict` for structured contracts
- CLI runner and Docker compatibility

## Components

- `agents/`
  - `market_data_agent.py` — returns structured market data
  - `sentiment_agent.py` — returns sentiment score and summary
  - `analyst_agent.py` — extracts analyst signals from mock reports
  - `aggregation_agent.py` — normalizes and merges upstream agent outputs
  - `backtesting_agent.py` — computes synthetic performance metrics
  - `decision_agent.py` — makes a final BUY/HOLD/SELL recommendation

- `orchestrator/pipeline.py`
  - Declarative workflow execution using a `WORKFLOW` list
  - Tracks agent input/output for transparent auditing

- `schemas/agent_models.py`
  - Defines typed data contracts for agent outputs and trace entries

- `data/mock_data.py`
  - Contains deterministic mock market, sentiment, analyst, and historical data

- `main.py`
  - CLI entrypoint
  - Prints stage-by-stage outputs, final decision, and execution trace

## Run locally

```bash
python3 main.py --ticker NVDA
```

## Docker

The existing `Dockerfile` remains compatible and can run the app as-is.

## Notes

This is intentionally a prototype, not a production system. The focus is on architecture, data flow, modularity, and future extensibility toward enterprise agent harnesses.
