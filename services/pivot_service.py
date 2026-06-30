def detect_pivots(candles, left=2, right=2):

    pivots = []

    total = len(candles)

    for i in range(left, total - right):

        current = candles[i]

        high = current["high"]
        low = current["low"]

        is_high = True
        is_low = True

        # Chap tomonni tekshirish
        for j in range(i - left, i):

            if candles[j]["high"] >= high:
                is_high = False

            if candles[j]["low"] <= low:
                is_low = False

        # O'ng tomonni tekshirish
        for j in range(i + 1, i + right + 1):

            if candles[j]["high"] >= high:
                is_high = False

            if candles[j]["low"] <= low:
                is_low = False

        # Natijani saqlash
        if is_high:
            pivots.append({
               
                "index": i,
                "type": "HIGH",
                "price": high,
                "strength": 0,
                "confirmed": False

            })

        if is_low:
            pivots.append({
                "index": i,
                "type": "LOW",
                "price": low,
                "strength": 0,
                "confirmed": False

            })

    return pivots

def score_pivots(candles, pivots):

    scored = []

    for pivot in pivots:

        strength = 0

        idx = pivot["index"]

        if pivot["type"] == "HIGH":

            future = candles[idx + 1: idx + 6]

            if future:

                lowest = min(c["low"] for c in future)

                impulse = pivot["price"] - lowest

                if impulse > 600:
                    strength = 4

                elif impulse > 300:
                    strength = 3

                elif impulse > 100:
                    strength = 2

                else:
                    strength = 1

        else:

            future = candles[idx + 1: idx + 6]

            if future:

                highest = max(c["high"] for c in future)

                impulse = highest - pivot["price"]

                if impulse > 600:
                    strength = 4

                elif impulse > 300:
                    strength = 3

                elif impulse > 100:
                    strength = 2

                else:
                    strength = 1

        pivot["strength"] = strength
        pivot["confirmed"] = strength >= 3

        scored.append(pivot)

    return scored