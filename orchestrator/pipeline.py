from agents.market_data_agent import MarketDataAgent
from agents.sentiment_agent import SentimentAgent
from agents.analyst_agent import AnalystReportAgent
from agents.backtesting_agent import BacktestingAgent
from agents.decision_agent import DecisionAgent


class TradingPipeline:
    """Simple orchestrator that executes the trading agent workflow."""

    def __init__(self) -> None:
        self.market_agent = MarketDataAgent()
        self.sentiment_agent = SentimentAgent()
        self.analyst_agent = AnalystReportAgent()
        self.backtesting_agent = BacktestingAgent()
        self.decision_agent = DecisionAgent()

    def run(self, ticker: str) -> dict:
        market_output = self.market_agent.run({"ticker": ticker})
        sentiment_output = self.sentiment_agent.run({"ticker": ticker})
        analyst_output = self.analyst_agent.run({"ticker": ticker})
        backtesting_output = self.backtesting_agent.run({"ticker": ticker})

        decision_input = {
            "market": market_output,
            "sentiment": sentiment_output,
            "analyst": analyst_output,
            "backtest": backtesting_output,
        }
        decision_output = self.decision_agent.run(decision_input)

        return {
            "ticker": ticker.upper(),
            "market": market_output,
            "sentiment": sentiment_output,
            "analyst": analyst_output,
            "backtest": backtesting_output,
            "decision": decision_output,
        }
