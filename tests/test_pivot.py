from services.binance_service import get_candles
from services.pivot_service import detect_pivots

candles = get_candles("BTCUSDT", "15m", 100)

pivots = detect_pivots(candles)

print(f"Pivotlar soni: {len(pivots)}")

for p in pivots:
    print(p)