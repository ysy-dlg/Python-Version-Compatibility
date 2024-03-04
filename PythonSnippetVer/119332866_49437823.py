def a():
 return 2 + 3

def b():
 return 3 - 2

def c():
 return 2*3

def d():
 return 2/3

dic = {}
dic['a'] = a
dic['b'] = b
dic['c'] = c
dic['d'] = d

funcs = str(raw_input("which functions would you like to use?: "))
funcs = funcs.split(',')

result = 0

for i in funcs:
 result += dic[i]()

print result