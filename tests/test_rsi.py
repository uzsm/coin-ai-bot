import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from services.binance_service import get_candles
from services.rsi_service import calculate_rsi

candles = get_candles("BTCUSDT", "15m", 300)

print(calculate_rsi(candles))