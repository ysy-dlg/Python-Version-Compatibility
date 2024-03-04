pattern=re.compile(r'(1[6][2]\.[0-9][0]+)')
seen = set()
if pattern.search(line):
    if line not in seen:
        seen.add(line)
        print line