def build_internal_structure(structure):

    if len(structure) < 2:
        return structure

    internal = [structure[0]]

    for current in structure[1:]:

        previous = internal[-1]

        # Bir xil label ketma-ket kelsa,
        # faqat oxirgisini qoldiramiz

        if current["label"] == previous["label"]:

            internal[-1] = current

        else:

            internal.append(current)

    return internal