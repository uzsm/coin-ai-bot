def build_major_swings(swings):

    if not swings:
        return []

    major = [swings[0]]

    for swing in swings[1:]:

        major.append(swing)

    return major