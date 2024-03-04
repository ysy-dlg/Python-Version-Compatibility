user_string = input() 
def accum(s):
    t = []  # list to store stuff into
    for count, letter in enumerate(s): 
        total = letter.upper() + letter * (count) # 1st as Upper, rest as is
        t.append(total)  # add to list
    print(*t, sep="-")   # the * "unpacks" the list into its parts

accum(user_string)