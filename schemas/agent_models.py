from typing import Any, Dict, List, TypedDict


class MarketDataOutput(TypedDict):
    ticker: str
    price: float
    trend: str
    basic_stats: Dict[str, Any]


class SentimentOutput(TypedDict):
    ticker: str
    sentiment_score: float
    sentiment_summary: str
    news_signals: List[Dict[str, Any]]


class AnalystOutput(TypedDict):
    ticker: str
    insights: List[Dict[str, str]]
    report_summary: str
    overall_sentiment: str


class AggregatedSignal(TypedDict):
    ticker: str
    market: MarketDataOutput
    sentiment: SentimentOutput
    analyst: AnalystOutput
    normalized: Dict[str, Any]


class DecisionOutput(TypedDict):
    decision: str
    confidence: float
    rationale: str
    scores: Dict[str, Any]


class BacktestOutput(TypedDict):
    ticker: str
    performance_metrics: Dict[str, Any]
    data_points: int


class AgentTraceStep(TypedDict):
    agent: str
    input: Dict[str, Any]
    output: Dict[str, Any]
