import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent))

from services.binance_service import get_candles
from services.pivot_service import detect_pivots
from services.swing_service import build_swings
from services.structure_service import (
    build_structure,
    analyze_structure
)

candles = get_candles("BTCUSDT", "15m", 100)

pivots = detect_pivots(candles)

swings = build_swings(pivots)

structure = build_structure(swings)

result = analyze_structure(structure)

print(result)