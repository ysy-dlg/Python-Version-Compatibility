import ast

#convert packed cells to list
indexes = df[df['colname'].apply(lambda x: not (isinstance(x, int) or isinstance(x, float)) and "," in x)].index
df.loc[indexes, 'colname'] = df.loc[indexes, 'colname'].apply(lambda x:ast.literal_eval( "[" + x +"]"))
#convert unpacked cells to list
indexes = df[df['colname'].apply(lambda x: isinstance(x, int) or isinstance(x, float))].index
df.loc[indexes, "colname"] = df.loc[indexes, "colname"].apply(lambda x: [x,])
#Recreate dataframe
vals = [[unique, *vals] for colname, *vals in df.values.tolist() for unique in colname]
df = pd.DataFrame(vals, columns = df.columns.tolist())
#Secure data type
df['colname'] = df['colname'].astype(float)
#Apply your function
df["colname"] = pd.to_datetime(df["colname"], unit='ms', utc=True)