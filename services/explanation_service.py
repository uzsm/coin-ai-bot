def explain_signal(result, signal):

    reasons = []

    if result["trend"] == "BULLISH":
        reasons.append("✅ Bullish Trend")

    elif result["trend"] == "BEARISH":
        reasons.append("✅ Bearish Trend")

    if result["stats"]["bos_count"] > 0:
        reasons.append("✅ BOS detected")
    else:
        reasons.append("❌ No BOS")

    if result.get("choch"):
        reasons.append("✅ ChoCH detected")
    else:
        reasons.append("❌ No ChoCH")

    return {

        "signal": signal["signal"],

        "confidence": signal["confidence"],

        "reasons": reasons

    }