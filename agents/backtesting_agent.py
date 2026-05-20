from data.mock_data import HISTORICAL_PRICE_SERIES


class BacktestingAgent:
    """Backtesting agent that computes basic performance metrics from synthetic price history."""

    def _calculate_metrics(self, prices: list[float]) -> dict:
        if len(prices) < 2:
            raise ValueError("At least two price points are required for backtesting")

        start_price = prices[0]
        end_price = prices[-1]
        total_return = (end_price - start_price) / start_price * 100

        returns = [
            (prices[i] - prices[i - 1]) / prices[i - 1]
            for i in range(1, len(prices))
        ]

        avg_return = sum(returns) / len(returns)
        variance = sum((r - avg_return) ** 2 for r in returns) / len(returns)
        volatility = variance ** 0.5 * 100

        peak = prices[0]
        max_drawdown = 0.0
        for price in prices:
            peak = max(peak, price)
            drawdown = (price - peak) / peak * 100
            max_drawdown = min(max_drawdown, drawdown)

        return {
            "return_pct": round(total_return, 2),
            "volatility_pct": round(volatility, 2),
            "max_drawdown_pct": round(max_drawdown, 2),
        }

    def run(self, input_dict: dict) -> dict:
        ticker = input_dict.get("ticker")
        historical_data = input_dict.get("historical_data")

        if historical_data is None:
            if not ticker:
                raise ValueError("BacktestingAgent requires ticker or historical_data")
            historical_data = HISTORICAL_PRICE_SERIES.get(ticker.upper(), HISTORICAL_PRICE_SERIES["DEFAULT"])

        metrics = self._calculate_metrics(historical_data)
        return {
            "ticker": ticker.upper() if ticker else None,
            "performance_metrics": metrics,
            "data_points": len(historical_data),
        }
