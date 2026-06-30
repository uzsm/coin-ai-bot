def build_swings(pivots):

    if not pivots:
        return []

    swings = [pivots[0]]

    for pivot in pivots[1:]:

        last = swings[-1]

        if pivot["type"] != last["type"]:
            swings.append(pivot)

        else:

            if pivot["type"] == "HIGH":

                if pivot["price"] > last["price"]:
                    swings[-1] = pivot

            else:

                if pivot["price"] < last["price"]:
                    swings[-1] = pivot

    return swings