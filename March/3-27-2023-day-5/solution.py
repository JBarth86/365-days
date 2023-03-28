def same_structure_as(original, other):

    if (
        # ensure valid external input
        # (internally same_structure_as() is only called with lists)
        not (isinstance(original, list) and isinstance(other, list))
        # and that those two list have the same length
        or (len(original) is not len(other))
    ):

        return False

    # we know at this point that both list have the same number of items
    for item in range(len(original)):

        # we check if both items are lists
        original_is_list = isinstance(original[item], list)
        other_is_list = isinstance(other[item], list)

        if (
                # if one item is a list and the other isn't ...
                original_is_list ^ other_is_list or
                # or if both items are lists but with different structures
                original_is_list and other_is_list and not
                same_structure_as(original[item], other[item])
        ):
            # then we return false, otherwise we check the next pair of items
            return False

    # if we get this far the structures are identical
    return True
