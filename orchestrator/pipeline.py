from typing import Any, Dict, List

from agents.analyst_agent import AnalystReportAgent
from agents.aggregation_agent import AggregationAgent
from agents.backtesting_agent import BacktestingAgent
from agents.decision_agent import DecisionAgent
from agents.market_data_agent import MarketDataAgent
from agents.sentiment_agent import SentimentAgent
from schemas.agent_models import AgentTraceStep


WORKFLOW = [
    "market",
    "sentiment",
    "analyst",
    "aggregation",
    "backtesting",
    "decision",
]


class TradingPipeline:
    """Orchestrator that executes a declarative workflow and captures execution trace."""

    def __init__(self) -> None:
        self.agents = {
            "market": MarketDataAgent(),
            "sentiment": SentimentAgent(),
            "analyst": AnalystReportAgent(),
            "aggregation": AggregationAgent(),
            "backtesting": BacktestingAgent(),
            "decision": DecisionAgent(),
        }

    def _build_step_input(self, step: str, ticker: str, outputs: Dict[str, Any]) -> Dict[str, Any]:
        if step == "market":
            return {"ticker": ticker}
        if step == "sentiment":
            return {"ticker": ticker}
        if step == "analyst":
            return {"ticker": ticker}
        if step == "aggregation":
            return {
                "market": outputs["market"],
                "sentiment": outputs["sentiment"],
                "analyst": outputs["analyst"],
            }
        if step == "backtesting":
            return {"ticker": ticker}
        if step == "decision":
            return {
                "aggregate": outputs["aggregation"],
                "backtest": outputs["backtesting"],
            }
        raise ValueError(f"Unknown workflow step: {step}")

    def run(self, ticker: str) -> Dict[str, Any]:
        trace: List[AgentTraceStep] = []
        outputs: Dict[str, Any] = {}

        for step in WORKFLOW:
            agent = self.agents[step]
            step_input = self._build_step_input(step, ticker, outputs)
            step_output = agent.run(step_input)

            trace.append({
                "agent": agent.__class__.__name__,
                "input": step_input,
                "output": step_output,
            })
            outputs[step] = step_output

        return {
            "result": outputs["decision"],
            "outputs": outputs,
            "trace": trace,
        }
