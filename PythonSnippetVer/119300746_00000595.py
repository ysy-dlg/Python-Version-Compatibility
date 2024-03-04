curs.execute('select max(x) from t')
maxValue = curs.fetchone()[0]