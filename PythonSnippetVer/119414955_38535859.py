# Each of your rows should be something like: 
list = ["string1", "string3", 1.435654, 4.43256]

#Round the floats
parsed_list = [round(x, 2) if i > 1 else x for i, x in enumerate(list)]
print parsed_list
['string1', 'string2', 1.44, 4.43]