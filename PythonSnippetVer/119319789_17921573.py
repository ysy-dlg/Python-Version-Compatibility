from collections import Counter, defaultdict
def findpattern():
    frequencies = defaultdict(Counter)
    for line in syslog:
        if re.search(r"regexforhostname",line):
            hostname= line.strip()[16:27]
            frequencies[hostname].update(f for f in word if f in line)
    return frequencies

result = findpattern()
for device, frequencies in result.iteritems():
    print '{}: {}'.format(
        device, 
        ', '.join(['{}x {}'.format(c, f) for f, c in frequencies.most_common()]))