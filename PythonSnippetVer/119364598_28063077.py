def counter():
    r = re.compile('[^0-9]')
    yield from (sum(map(int, r.sub('', x))) for x in self.get_xs()) 