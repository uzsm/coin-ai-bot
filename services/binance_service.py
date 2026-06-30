import requests

BASE_URL = "https://api.binance.com"


def get_klines(symbol, interval, limit=200):

    url = f"{BASE_URL}/api/v3/klines"

    params = {
        "symbol": symbol,
        "interval": interval,
        "limit": limit
    }

    response = requests.get(
        url,
        params=params,
        timeout=10
    )

    response.raise_for_status()

    return response.json()
def get_candles(symbol, interval, limit=200):

    raw = get_klines(symbol, interval, limit)

    candles = []

    for c in raw:

        candles.append({

            "open_time": c[0],

            "open": float(c[1]),

            "high": float(c[2]),

            "low": float(c[3]),

            "close": float(c[4]),

            "volume": float(c[5]),

            "close_time": c[6]

        })

    return candles