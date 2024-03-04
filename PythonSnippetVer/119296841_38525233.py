def maxElement(L):
    length=len(L)
    if length == 1:
        # Have this condition on the top because you are using length - 2 later
        # Just return the only element
        return L

    if L[length-1] > L[length-2]:
        # If the last element is greater than the last but one, delete the last but one
        del L[length - 2]
    else:
        # Simple else would suffice because you are just checking for the opposite
        # Also this condition saves you from:
        #       infinite looping when the last two elements are equal
        del L[length - 1]
    print L
    # Time to call it recursively.
    # But if you just don't want to unnecessarily increase the recursion
    # tree depth, check for length and return it
    if length == 1:
        return L
    return maxElement(L)