def calculate_confidence(

    trend,
    indicators,
    bos,
    choch,
    order_blocks

):

    score = 50

    reasons = []

    # =====================================
    # Trend
    # =====================================

    if trend == "BULLISH":

        score += 10
        reasons.append("Bullish Trend")

    elif trend == "BEARISH":

        score -= 10
        reasons.append("Bearish Trend")

    # =====================================
    # EMA
    # =====================================

    ema20 = indicators["ema20"]
    ema50 = indicators["ema50"]
    ema200 = indicators["ema200"]

    if ema20 > ema50 > ema200:

        score += 10
        reasons.append("EMA Bullish")

    elif ema20 < ema50 < ema200:

        score -= 10
        reasons.append("EMA Bearish")

    # =====================================
    # RSI
    # =====================================

    rsi = indicators["rsi"]

    if 45 <= rsi <= 65:

        score += 8
        reasons.append("Healthy RSI")

    elif rsi > 70:

        score -= 8
        reasons.append("Overbought")

    elif rsi < 30:

        score += 6
        reasons.append("Oversold")

    # =====================================
    # MACD
    # =====================================

    if indicators["macd"] > indicators["macd_signal"]:

        score += 8
        reasons.append("MACD Bullish")

    else:

        score -= 8
        reasons.append("MACD Bearish")

    # =====================================
    # BOS
    # =====================================

    if len(bos):

        score += min(len(bos) * 2, 10)

        reasons.append(f"BOS x{len(bos)}")

    # =====================================
    # CHOCH
    # =====================================

    if len(choch):

        score += min(len(choch) * 3, 10)

        reasons.append(f"CHOCH x{len(choch)}")

    # =====================================
    # Order Block
    # =====================================

    if len(order_blocks):

        score += min(len(order_blocks) * 2, 10)

        reasons.append("Order Block")

    # =====================================
    # Clamp
    # =====================================

    score = max(0, min(score, 100))

    # =====================================
    # Recommendation
    # =====================================

    if score >= 80:

        signal = "STRONG BUY"

    elif score >= 65:

        signal = "BUY"

    elif score >= 45:

        signal = "NEUTRAL"

    elif score >= 30:

        signal = "SELL"

    else:

        signal = "STRONG SELL"

    return {

        "score": score,

        "signal": signal,

        "reasons": reasons

    }