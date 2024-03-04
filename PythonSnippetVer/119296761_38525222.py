def maxElement(L):
	length=len(L)
	if length == 1:
		return L
	elif L[length-1]>=L[length-2]:
	    del L[length-2]
	elif L[length-1]<=L[length-2]:
	    del L[length-1]	
	return maxElement(L)    

print maxElement([1,2,95754754745,3,1,8,444,2,42425])