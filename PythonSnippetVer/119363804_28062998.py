n = int(raw_input())
left = int(raw_input())
memo = {}
def dp(n, left): # returns tuple (cost, [factors])
    if (n, left) in memo: return memo[(n, left)]
    if left == 1:
	    return (n, [n])
    i = 2
    best = n
    bestTuple = [n]
    while i * i <= n:
	    if n % i == 0:
	        rem = dp(n / i, left - 1)
	        if rem[0] + i < best:
	            best = rem[0] + i
	            bestTuple = [i] + rem[1]
	    i += 1
    memo[(n, left)] = (best, bestTuple)
    return memo[(n, left)]
print dp(n, left)[1]