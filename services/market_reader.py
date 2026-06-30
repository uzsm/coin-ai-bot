def prepare_market(candles):

    market = []

    for i, candle in enumerate(candles):

        body = abs(candle["close"] - candle["open"])

        upper_wick = candle["high"] - max(
            candle["open"],
            candle["close"]
        )

        lower_wick = min(
            candle["open"],
            candle["close"]
        ) - candle["low"]

        market.append({

            "index": i,

            "open": candle["open"],

            "high": candle["high"],

            "low": candle["low"],

            "close": candle["close"],

            "volume": candle["volume"],

            "body": body,

            "upper_wick": upper_wick,

            "lower_wick": lower_wick,

            "bullish": candle["close"] > candle["open"]

        })

    return market