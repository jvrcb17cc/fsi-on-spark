MARKET_DATA = {
    "ACME": {
        "price": 142.25,
        "trend": "up",
        "52_week_high": 155.0,
        "52_week_low": 102.3,
        "avg_volume": 1_250_000,
    },
    "GLBX": {
        "price": 88.5,
        "trend": "down",
        "52_week_high": 112.0,
        "52_week_low": 76.4,
        "avg_volume": 880_000,
    },
    "WAZ": {
        "price": 39.7,
        "trend": "flat",
        "52_week_high": 48.2,
        "52_week_low": 29.1,
        "avg_volume": 430_000,
    },
    "DEFAULT": {
        "price": 100.0,
        "trend": "flat",
        "52_week_high": 110.0,
        "52_week_low": 90.0,
        "avg_volume": 500_000,
    },
}

NEWS_SENTIMENT = {
    "ACME": [
        {"headline": "ACME beats estimates on strong demand", "score": 0.4},
        {"headline": "ACME expands into new markets", "score": 0.3},
        {"headline": "ACME faces supply chain pressure", "score": -0.1},
    ],
    "GLBX": [
        {"headline": "GLBX revenue outlook is lower than expected", "score": -0.4},
        {"headline": "GLBX executing cost reduction plan", "score": 0.1},
        {"headline": "GLBX shares slide on macro concern", "score": -0.3},
    ],
    "WAZ": [
        {"headline": "WAZ keeps guidance steady despite volatility", "score": 0.0},
        {"headline": "WAZ sees interest from strategic buyers", "score": 0.2},
        {"headline": "WAZ execution risk remains moderate", "score": -0.1},
    ],
    "DEFAULT": [
        {"headline": "Market commentary remains balanced", "score": 0.0},
    ],
}

ANALYST_REPORTS = {
    "ACME": (
        "Analyst note: ACME is positioned to outperform the sector next quarter. "
        "Revenue expansion and margin improvement remain the primary bullish drivers."
    ),
    "GLBX": (
        "Analyst note: GLBX faces near-term headwinds from slower demand and cost pressures. "
        "We remain cautious until guidance stabilizes."
    ),
    "WAZ": (
        "Analyst note: WAZ shows mixed signals with moderate growth and execution risk. "
        "The stock is likely to trade sideways until visibility improves."
    ),
    "DEFAULT": "Analyst report is neutral and recommends waiting for clearer signals.",
}

HISTORICAL_PRICE_SERIES = {
    "ACME": [110.0, 115.5, 120.2, 127.8, 132.0, 137.5, 142.3],
    "GLBX": [95.0, 92.1, 89.8, 86.0, 84.5, 82.0, 88.5],
    "WAZ": [40.0, 39.8, 40.5, 39.9, 40.1, 40.0, 39.7],
    "DEFAULT": [100.0, 100.5, 99.8, 100.2, 100.0, 100.1],
}
