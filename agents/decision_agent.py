class DecisionAgent:
    """Decision agent that combines upstream signals into a final recommendation."""

    def run(self, input_dict: dict) -> dict:
        market = input_dict.get("market", {})
        sentiment = input_dict.get("sentiment", {})
        analyst = input_dict.get("analyst", {})
        backtest = input_dict.get("backtest", {})

        trend_score = 1 if market.get("trend") == "up" else -1 if market.get("trend") == "down" else 0
        sentiment_score = sentiment.get("sentiment_score", 0)
        analyst_score = 1 if analyst.get("overall_sentiment") == "bullish" else -1 if analyst.get("overall_sentiment") == "bearish" else 0

        perf = backtest.get("performance_metrics", {})
        return_pct = perf.get("return_pct", 0)
        drawdown = perf.get("max_drawdown_pct", 0)
        backtest_score = 1 if return_pct > 0 and drawdown > -10 else -1 if return_pct < 0 else 0

        total_score = trend_score + sentiment_score + analyst_score + backtest_score

        if total_score >= 2:
            decision = "BUY"
            rationale = "Multiple data signals align on an upward opportunity."
        elif total_score <= -2:
            decision = "SELL"
            rationale = "Market, sentiment, analyst, and backtest signals suggest caution."
        else:
            decision = "HOLD"
            rationale = "Signals are mixed; preserve capital while watching further data."

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
