p = re.compile('((:?0000)+)')
longestword = ""
for word in p.findall(ip6):
    if len(word[0])>len(longestword):
        longestword = word[0]
print longestword

