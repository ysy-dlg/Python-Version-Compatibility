import ast
for colname in ['Date', 'Created']:
	#convert packed cells to list
	indexes = df[df[colname].apply(lambda x: not (isinstance(x, int) or isinstance(x, float)) and "," in x)].index
	df.loc[indexes, colname] = df.loc[indexes, colname].apply(lambda x:ast.literal_eval( "[" + x +"]"))

	#convert unpacked cells to list
	indexes = df[df[colname].apply(lambda x: isinstance(x, int) or isinstance(x, float))].index
	df.loc[indexes, colname] = df.loc[indexes, colname].apply(lambda x: [x,])

vals = [[userid, visit, unique_date, uniquefilename, unique_created, *rest_of_datas] for userid, visit, date, uniquefilename, created, *rest_of_datas in df.values.tolist() for unique_date in date for unique_created in created]
df = pd.DataFrame(vals, columns = df.columns.tolist())
for colname in ['Date', 'Created']:
	df[colname] = pd.to_datetime(df[colname], unit='ms', utc=True)