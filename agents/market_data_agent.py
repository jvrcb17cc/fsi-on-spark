from data.mock_data import MARKET_DATA


class MarketDataAgent:
    """Market data agent that returns structured, deterministic ticker statistics."""

    def run(self, input_dict: dict) -> dict:
        ticker = input_dict.get("ticker")
        if not ticker:
            raise ValueError("MarketDataAgent requires a ticker in input_dict")

        payload = MARKET_DATA.get(ticker.upper(), MARKET_DATA["DEFAULT"])
        return {
            "ticker": ticker.upper(),
            "price": payload["price"],
            "trend": payload["trend"],
            "basic_stats": {
                "52_week_high": payload["52_week_high"],
                "52_week_low": payload["52_week_low"],
                "avg_volume": payload["avg_volume"],
            },
        }
