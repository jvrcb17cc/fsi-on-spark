from orchestrator.pipeline import TradingPipeline


def format_section(title: str, content: dict) -> str:
    lines = [f"=== {title} ==="]
    for key, value in content.items():
        lines.append(f"{key}: {value}")
    return "\n".join(lines)


def print_pipeline_result(result: dict) -> None:
    print(format_section("Market Data", result["market"]))
    print()
    print(format_section("Sentiment", result["sentiment"]))
    print()
    print(format_section("Analyst Report", {
        "overall_sentiment": result["analyst"]["overall_sentiment"],
        "insights": result["analyst"]["insights"],
    }))
    print()
    print(format_section("Backtesting", result["backtest"]["performance_metrics"]))
    print()
    print(format_section("Decision", result["decision"]))


def main() -> None:
    ticker = "NVDA"
    print(f"Running trading pipeline for ticker: {ticker}\n")

    pipeline = TradingPipeline()
    result = pipeline.run(ticker)

    print_pipeline_result(result)


if __name__ == "__main__":
    main()
