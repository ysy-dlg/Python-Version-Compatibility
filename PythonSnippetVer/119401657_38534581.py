from difflib import unified_diff

s1 = ['a', 'b', 'c', 'd', 'e', 'f']
s2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'i', 'k', 'l', 'm', 'n']

for line in unified_diff(s1, s2,n=6):
    print line