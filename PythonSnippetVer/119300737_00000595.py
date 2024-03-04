curs.execute('select * from people')
for row in curs:
    print row