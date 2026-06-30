from services.binance_service import get_candles
from services.market_reader import prepare_market

candles = get_candles("BTCUSDT", "15m", 3)

market = prepare_market(candles)

for c in market:
    print(c)