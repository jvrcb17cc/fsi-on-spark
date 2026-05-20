from schemas.agent_models import AggregatedSignal, BacktestOutput, DecisionOutput


class DecisionAgent:
    """Decision agent that consumes normalized aggregate signals and backtest metrics."""

    def run(self, input_dict: dict) -> DecisionOutput:
        aggregate = input_dict.get("aggregate", {})
        backtest = input_dict.get("backtest", {})

        if not isinstance(aggregate, dict) or not isinstance(backtest, dict):
            raise ValueError("DecisionAgent requires aggregate and backtest outputs")

        normalized = aggregate.get("normalized", {})
        trend_score = 1 if normalized.get("trend") == "up" else -1 if normalized.get("trend") == "down" else 0
        sentiment_score = normalized.get("sentiment_score", 0.0)
        analyst_score = 1 if normalized.get("analyst_signal") == "bullish" else -1 if normalized.get("analyst_signal") == "bearish" else 0

        perf = backtest.get("performance_metrics", {})
        return_pct = perf.get("return_pct", 0.0)
        drawdown = perf.get("max_drawdown_pct", 0.0)
        backtest_score = 1 if return_pct > 0 and drawdown > -10 else -1 if return_pct < 0 else 0

        total_score = trend_score + sentiment_score + analyst_score + backtest_score

        if total_score >= 2:
            decision = "BUY"
            rationale = "Multiple normalized signals point to an upward opportunity."
        elif total_score <= -2:
            decision = "SELL"
            rationale = "Normalized signals and backtest metrics recommend caution."
        else:
            decision = "HOLD"
            rationale = "Signals are mixed; maintain position until further clarity."

        confidence = min(1.0, max(0.2, abs(total_score) / 4))

        return {
            "decision": decision,
            "confidence": round(confidence, 2),
            "rationale": rationale,
            "scores": {
                "trend_score": trend_score,
                "sentiment_score": sentiment_score,
                "analyst_score": analyst_score,
                "backtest_score": backtest_score,
                "total_score": round(total_score, 2),
            },
        }
