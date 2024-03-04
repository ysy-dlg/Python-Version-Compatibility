row = curs.fetchone()
while row:
    print row
    row = curs.fetchone()