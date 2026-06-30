from services.binance_service import get_candles

candles = get_candles(
    "BTCUSDT",
    "15m",
    3
)

for candle in candles:
    print(candle)