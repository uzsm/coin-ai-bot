def generate_signal(result):

    trend = result["trend"]

    bos_count = result["stats"]["bos_count"]

    if trend == "BULLISH" and bos_count > 0:

        return {
            "signal": "BUY",
            "confidence": 70
        }

    elif trend == "BEARISH" and bos_count > 0:

        return {
            "signal": "SELL",
            "confidence": 70
        }

    return {
        "signal": "WAIT",
        "confidence": 50
    }