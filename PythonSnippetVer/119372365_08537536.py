l = ['A', 'AA', 'B', 'BB', 'C', 'CC']
l.sort(key=lambda element: (len(element), element))
print l
['A', 'B', 'C', 'AA', 'BB', 'CC']