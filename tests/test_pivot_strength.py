import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.binance_service import get_candles
from services.pivot_service import detect_pivots, score_pivots

candles = get_candles("BTCUSDT", "15m", 100)

pivots = detect_pivots(candles)

scored = score_pivots(candles, pivots)

for p in scored:
    print(
        p["type"],
        p["price"],
        "Strength:",
        p["strength"],
        "Confirmed:",
        p["confirmed"]
    )