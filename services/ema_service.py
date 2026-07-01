import pandas as pd


def calculate_ema(candles):

    df = pd.DataFrame(candles)

    close = df["close"]

    ema20 = close.ewm(span=20).mean().iloc[-1]

    ema50 = close.ewm(span=50).mean().iloc[-1]

    ema200 = close.ewm(span=200).mean().iloc[-1]

    trend = "NEUTRAL"

    if ema20 > ema50 > ema200:
        trend = "STRONG_BULLISH"

    elif ema20 < ema50 < ema200:
        trend = "STRONG_BEARISH"

    return {

        "ema20": round(float(ema20), 2),

        "ema50": round(float(ema50), 2),

        "ema200": round(float(ema200), 2),

        "trend": trend

    }