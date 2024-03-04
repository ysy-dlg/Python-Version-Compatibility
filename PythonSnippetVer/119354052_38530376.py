url="http://example.com/ru/path/?id=1234&var=abcd"
if url.split('?')[1].startswith('id=') and url.split('&')[1].startswith('var='):
    print "yay!"