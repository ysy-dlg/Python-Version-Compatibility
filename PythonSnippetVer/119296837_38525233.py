def maxElement(L):
    length=len(L)
    if L[length-1]>L[length-2]:
        del L[length-2]
        print L
    elif L[length-1]<L[length-2]:
        del L[length-1]
    if len(L) == 1:
        return L
    return maxElement(L)
print maxElement([1,2,95754754745,3,1,8,444,2,42425])