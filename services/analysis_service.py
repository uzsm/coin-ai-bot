from services.binance_service import get_candles
from services.pivot_service import detect_pivots
from services.swing_service import build_swings
from services.structure_service import build_structure
from services.trend_service import detect_trend
from services.bos_service import detect_bos


def analyze(symbol, timeframe):

    candles = get_candles(symbol, timeframe, 100)

    pivots = detect_pivots(candles)

    swings = build_swings(pivots)

    structure = build_structure(swings)

    trend = detect_trend(structure)

    bos = detect_bos(structure, candles)

    return {

        "trend": trend,

        "pivot_count": len(pivots),

        "swing_count": len(swings),

        "structure_count": len(structure),

        "bos_count": len(bos)

    }