import pandas as pd


def calculate_indicators(candles):

    df = pd.DataFrame(candles)

    close = df["close"]
    high = df["high"]
    low = df["low"]
    volume = df["volume"]

    # =====================================
    # EMA
    # =====================================

    ema20 = close.ewm(span=20).mean().iloc[-1]
    ema50 = close.ewm(span=50).mean().iloc[-1]
    ema200 = close.ewm(span=200).mean().iloc[-1]

    # =====================================
    # RSI
    # =====================================

    delta = close.diff()

    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    # =====================================
    # MACD
    # =====================================

    ema12 = close.ewm(span=12).mean()
    ema26 = close.ewm(span=26).mean()

    macd = ema12 - ema26

    signal = macd.ewm(span=9).mean()

    histogram = macd - signal

    # =====================================
    # ATR
    # =====================================

    tr1 = high - low
    tr2 = (high - close.shift()).abs()
    tr3 = (low - close.shift()).abs()

    tr = pd.concat([tr1, tr2, tr3], axis=1).max(axis=1)

    atr = tr.rolling(14).mean()

    # =====================================
    # Volume
    # =====================================

    avg_volume = volume.tail(20).mean()

    last_volume = volume.iloc[-1]

    volume_percent = (last_volume / avg_volume) * 100

    return {

        "ema20": round(float(ema20), 2),

        "ema50": round(float(ema50), 2),

        "ema200": round(float(ema200), 2),

        "rsi": round(float(rsi.iloc[-1]), 2),

        "macd": round(float(macd.iloc[-1]), 4),

        "macd_signal": round(float(signal.iloc[-1]), 4),

        "macd_histogram": round(float(histogram.iloc[-1]), 4),

        "atr": round(float(atr.iloc[-1]), 2),

        "volume_percent": round(float(volume_percent), 1)

    }