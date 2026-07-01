import pandas as pd


def calculate_rsi(candles, period=14):

    df = pd.DataFrame(candles)

    close = df["close"]

    delta = close.diff()

    gain = delta.where(delta > 0, 0)

    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(period).mean()

    avg_loss = loss.rolling(period).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    value = round(float(rsi.iloc[-1]), 2)

    signal = "NEUTRAL"

    if value >= 70:
        signal = "OVERBOUGHT"

    elif value <= 30:
        signal = "OVERSOLD"

    return {

        "rsi": value,

        "signal": signal

    }