from data.mock_data import NEWS_SENTIMENT
from schemas.agent_models import SentimentOutput


class SentimentAgent:
    """Sentiment agent that evaluates a mock news dataset and returns a score."""

    def run(self, input_dict: dict) -> SentimentOutput:
        ticker = input_dict.get("ticker")
        if not ticker:
            raise ValueError("SentimentAgent requires a ticker in input_dict")

        dataset = NEWS_SENTIMENT.get(ticker.upper(), NEWS_SENTIMENT["DEFAULT"])
        score_values = [item["score"] for item in dataset]
        average_score = sum(score_values) / len(score_values)

        if average_score > 0.2:
            summary = "Sentiment is positive with constructive news flow."
        elif average_score < -0.2:
            summary = "Sentiment is negative with cautionary headlines."
        else:
            summary = "Sentiment remains neutral with balanced coverage."

        return {
            "ticker": ticker.upper(),
            "sentiment_score": round(average_score, 3),
            "sentiment_summary": summary,
            "news_signals": dataset,
        }
