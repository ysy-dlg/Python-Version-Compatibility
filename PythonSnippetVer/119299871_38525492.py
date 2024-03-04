s = [{'name': 'Bart', 'age': 12}, {'name': 'Bart', 'age': 19}, {'name': 'Bart', 'age': 1},
    {'name': 'Homer', 'age': 30}, {'name': 'Homer', 'age': 12},{'name': 'Simpson', 'age': 19}]

res=[]

for m,n in zip(s, reversed(s)):
	if m!=n:
		res.append(m)
		res.append(n)
	else:		
		res.append(m)
	if len(res)==len(s):
		break

print res