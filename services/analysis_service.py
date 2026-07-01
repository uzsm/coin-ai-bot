from services.binance_service import get_candles
from services.pivot_service import detect_pivots
from services.swing_service import build_swings
from services.structure_service import (
    build_structure,
    analyze_structure
)
from services.bos_service import detect_bos
from services.order_block_service import detect_order_blocks
from services.indicator_service import calculate_indicators
from services.confidence_service import calculate_confidence
 


def analyze(symbol, timeframe):

    candles = get_candles(symbol, timeframe, 100)

    pivots = detect_pivots(candles)

    swings = build_swings(pivots)

    structure = build_structure(swings)

    structure_info = analyze_structure(structure)

    bos = detect_bos(structure, candles)
    
    order_blocks = detect_order_blocks(candles, bos)
    
    indicators = calculate_indicators(candles)
    
    last_price = candles[-1]["close"]
    
    confidence = calculate_confidence(

    structure_info["trend"],

    indicators,

    bos,

    [],      # hozircha choch

    order_blocks

)

    return {
       

        "symbol": symbol,

        "timeframe": timeframe,

        "trend": structure_info["trend"],

        "analysis": structure_info,

        "candles": candles,

        "pivots": pivots,

        "swings": swings,

        "structure": structure,

        "bos": bos,

        "order_blocks": order_blocks,

        "indicators": indicators,

        "last_price": last_price,
        
        "confidence": confidence,

        "stats": {

            "pivot_count": len(pivots),

            "swing_count": len(swings),

            "structure_count": len(structure),

            "bos_count": len(bos),
            
            "order_block_count": len(order_blocks)

        }

    }