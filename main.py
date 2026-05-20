import argparse
import json
from typing import Any, Dict

from orchestrator.pipeline import TradingPipeline


def print_section(title: str, data: Dict[str, Any]) -> None:
    print(f"=== {title} ===")
    print(json.dumps(data, indent=2))
    print()


def main() -> None:
    parser = argparse.ArgumentParser(description="Run the trading multi-agent pipeline.")
    parser.add_argument("--ticker", default="NVDA", help="Ticker symbol to analyze")
    args = parser.parse_args()

    ticker = args.ticker.upper()
    print(f"Running trading pipeline for ticker: {ticker}\n")

    pipeline = TradingPipeline()
    result = pipeline.run(ticker)

    for stage, output in result["outputs"].items():
        print_section(f"Stage: {stage}", output)

    print_section("Final Decision", result["result"])
    print_section("Execution Trace", {"trace": result["trace"]})


if __name__ == "__main__":
    main()
