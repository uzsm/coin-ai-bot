from services.binance_service import get_candles
from services.pivot_service import detect_pivots
from services.swing_service import build_swings

candles = get_candles("BTCUSDT", "15m", 100)

pivots = detect_pivots(candles)

swings = build_swings(pivots)

print(f"Pivotlar : {len(pivots)}")
print(f"Swinglar : {len(swings)}")

for s in swings:
    print(s)