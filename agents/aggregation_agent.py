from schemas.agent_models import AggregatedSignal, AnalystOutput, MarketDataOutput, SentimentOutput


class AggregationAgent:
    """Aggregation agent that normalizes and combines upstream structured signals."""

    def run(self, input_dict: dict) -> AggregatedSignal:
        market = input_dict.get("market")
        sentiment = input_dict.get("sentiment")
        analyst = input_dict.get("analyst")

        if not isinstance(market, dict) or not isinstance(sentiment, dict) or not isinstance(analyst, dict):
            raise ValueError("AggregationAgent requires market, sentiment, and analyst outputs")

        normalized_sentiment = round(sentiment.get("sentiment_score", 0.0), 3)
        normalized_trend = market.get("trend", "flat")
        confidence_signals = {
            "trend": normalized_trend,
            "sentiment_score": normalized_sentiment,
            "analyst_signal": analyst.get("overall_sentiment", "neutral"),
        }

        return {
            "ticker": market.get("ticker", "UNKNOWN"),
            "market": market,  # type: ignore[assignment]
            "sentiment": sentiment,  # type: ignore[assignment]
            "analyst": analyst,  # type: ignore[assignment]
            "normalized": confidence_signals,
        }
