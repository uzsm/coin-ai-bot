import sys
from pathlib import Path

# Loyiha ildizini Python path ga qo'shamiz
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from services.binance_service import get_candles
from services.ema_service import calculate_ema

candles = get_candles("BTCUSDT", "15m", 300)

result = calculate_ema(candles)

print(result)