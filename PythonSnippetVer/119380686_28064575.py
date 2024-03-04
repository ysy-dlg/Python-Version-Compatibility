areas = pd.pivot_table(df[df['NaturalDisaster']=='Fire'],
                       values='NaturalDisaster', 
                       index='Area', 
                       aggfunc='count')