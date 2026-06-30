def calculate_score(result):

    score = 50
    reasons = []

    # Trend
    if result["trend"] == "BULLISH":
        score += 20
        reasons.append("✅ Bullish Trend")

    elif result["trend"] == "BEARISH":
        score -= 20
        reasons.append("✅ Bearish Trend")

    # BOS
    bos_count = result["stats"]["bos_count"]

    if bos_count > 0:

        if result["trend"] == "BULLISH":
            score += 20

        elif result["trend"] == "BEARISH":
            score -= 20

        reasons.append(f"✅ BOS x {bos_count}")

    # Chegaralash
    score = max(0, min(100, score))

    return {

        "score": score,

        "reasons": reasons

    }