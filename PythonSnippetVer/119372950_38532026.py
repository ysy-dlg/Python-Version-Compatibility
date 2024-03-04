import dateutil

df = pd.read_csv('Test.csv', index_col=0, parse_dates=True, date_parser=dateutil.parser.parse)

print(df)