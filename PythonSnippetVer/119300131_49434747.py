res = df.groupby(df['List'].map(tuple))['Count'].sum()
res['List'] = res['List'].map(list)

#            List  Count
# 0     [a, time]      6
# 1  [once, upon]      5
# 2  [there, was]      1