my_str = " ".join([a.strip() for a in b.split("\n") if a])
print '"' + my_str + '"' #Use single quotes to surround the double quotes
"a b c d e f g"
print "\"" + my_str + "\"" #Escape the double quotes
"a b c d e f g"
print '"%s"'%my_str #Use string formatting
"a b c d e f g"