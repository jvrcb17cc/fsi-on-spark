from data.mock_data import ANALYST_REPORTS
from schemas.agent_models import AnalystOutput


class AnalystReportAgent:
    """Analyst report agent that extracts structured signals from mock research text."""

    def _parse_signals(self, report_text: str) -> dict:
        bullish_keywords = ["outperform", "expansion", "upgrade", "positive", "growth"]
        bearish_keywords = ["downgrade", "concern", "risk", "slowdown", "weakness"]

        bullish_count = sum(1 for word in bullish_keywords if word in report_text.lower())
        bearish_count = sum(1 for word in bearish_keywords if word in report_text.lower())

        if bullish_count > bearish_count:
            overall = "bullish"
        elif bearish_count > bullish_count:
            overall = "bearish"
        else:
            overall = "neutral"

        return {
            "bullish_count": bullish_count,
            "bearish_count": bearish_count,
            "overall_sentiment": overall,
        }

    def run(self, input_dict: dict) -> AnalystOutput:
        report_text = input_dict.get("report_text")
        ticker = input_dict.get("ticker")

        if not report_text and not ticker:
            raise ValueError("AnalystReportAgent requires ticker or report_text in input_dict")

        if not report_text:
            report_text = ANALYST_REPORTS.get(ticker.upper(), ANALYST_REPORTS["DEFAULT"])

        signals = self._parse_signals(report_text)
        insights = []

        if signals["overall_sentiment"] == "bullish":
            insights.append({"signal": "Bullish", "reason": "Report contains more positive language than negative."})
        elif signals["overall_sentiment"] == "bearish":
            insights.append({"signal": "Bearish", "reason": "Report includes several risk and slowdown warnings."})
        else:
            insights.append({"signal": "Neutral", "reason": "Report language is balanced between opportunities and risks."})

        return {
            "ticker": ticker.upper() if ticker else "UNKNOWN",
            "insights": insights,
            "report_summary": report_text,
            "overall_sentiment": signals["overall_sentiment"],
        }
