from itertools import groupby

ip6 = "1234:0678:0000:0000:00cd:0000:0000:0000"

longest = 0
for section, elems in groupby(ip6.split(':')):
    if section == '0000':
        longest = len(list(elems))

print longest  # Prints '3', the number of times '0000' repeats the most.
               # you could, of course, generate a string of 0000:... from this