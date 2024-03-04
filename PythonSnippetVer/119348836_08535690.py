In [1]: l = [(1, 3), (6, 7)]

In [2]: s = 'AABBCCDD'

In [3]: ''.join(s[start-1:end] for (start,end) in l)
Out[3]: 'AABCD'