d = pd.concat(dfs1).groupby(level=1).apply(list).to_dict()
print (d)
{'2017-05-22': [56, 44], '2017-05-21': [33, 5], '2017-05-20': [33, 46]}