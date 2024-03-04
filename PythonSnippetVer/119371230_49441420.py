def my_fun (var1,var2,var3,var4):
    df[var4]= np.where(df[var1] & df[var3].eq('eggs') & df[var2].lt(10),
                       'hello', 'zello')
    return df