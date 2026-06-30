def find_swings(candles, left=2, right=2):

    swings = []

    total = len(candles)

    for i in range(left, total - right):

        current = candles[i]

        high = current["high"]
        low = current["low"]

        swing_high = True
        swing_low = True
            # Chap tomonni tekshirish

        for j in range(i - left, i):

            if candles[j]["high"] >= high:
                swing_high = False

            if candles[j]["low"] <= low:
                swing_low = False    
                # O'ng tomonni tekshirish

        for j in range(i + 1, i + right + 1):

            if candles[j]["high"] >= high:
                swing_high = False

            if candles[j]["low"] <= low:
                swing_low = False 
               
    if swing_high:

            swings.append({

                "index": i,

                "type": "HIGH",

                "price": high

            })


    if swing_low:

            swings.append({

                "index": i,

                "type": "LOW",

                "price": low

            })

    return swings               