def detect_order_blocks(candles, bos):

    order_blocks = []

    if not bos:
        return order_blocks

    for signal in bos:

        break_index = signal["break_index"]

        if signal["type"] == "BULLISH":

            # BOS oldidagi oxirgi bearish candle
            for i in range(break_index - 1, -1, -1):

                candle = candles[i]

                if candle["close"] < candle["open"]:

                    order_blocks.append({

                        "type": "BULLISH",

                        "index": i,

                        "high": candle["high"],

                        "low": candle["low"]

                    })

                    break

        else:

            # BOS oldidagi oxirgi bullish candle
            for i in range(break_index - 1, -1, -1):

                candle = candles[i]

                if candle["close"] > candle["open"]:

                    order_blocks.append({

                        "type": "BEARISH",

                        "index": i,

                        "high": candle["high"],

                        "low": candle["low"]

                    })

                    break

    return order_blocks