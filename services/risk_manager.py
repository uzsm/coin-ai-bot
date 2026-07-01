def calculate_trade_levels(
    trend,
    price,
    indicators,
    order_blocks,
):

    atr = indicators["atr"]

    entry = None
    stop_loss = None

    take_profit_1 = None
    take_profit_2 = None
    take_profit_3 = None

    risk_reward = 0

    # ======================================
    # BUY
    # ======================================

    if trend == "BULLISH":

        if order_blocks:

            ob = order_blocks[-1]

            entry = round((ob["high"] + ob["low"]) / 2, 2)

            stop_loss = round(ob["low"] - atr * 0.5, 2)

        else:

            entry = round(price, 2)

            stop_loss = round(price - atr, 2)

        risk = entry - stop_loss

        take_profit_1 = round(entry + risk * 2, 2)

        take_profit_2 = round(entry + risk * 3, 2)

        take_profit_3 = round(entry + risk * 5, 2)

        risk_reward = "1:5"

    # ======================================
    # SELL
    # ======================================

    elif trend == "BEARISH":

        if order_blocks:

            ob = order_blocks[-1]

            entry = round((ob["high"] + ob["low"]) / 2, 2)

            stop_loss = round(ob["high"] + atr * 0.5, 2)

        else:

            entry = round(price, 2)

            stop_loss = round(price + atr, 2)

        risk = stop_loss - entry

        take_profit_1 = round(entry - risk * 2, 2)

        take_profit_2 = round(entry - risk * 3, 2)

        take_profit_3 = round(entry - risk * 5, 2)

        risk_reward = "1:5"

    return {

        "entry": entry,

        "stop_loss": stop_loss,

        "tp1": take_profit_1,

        "tp2": take_profit_2,

        "tp3": take_profit_3,

        "risk_reward": risk_reward

    }