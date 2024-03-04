from io import StringIO

import pandas as pd
import matplotlib.pyplot as plt


s = '''Date, Area, NaturalDisaster
12/10/2009, A, Fire
12/13/2009, B, Flood
01/12/2010, B, Fire
05/01/2011, A, Fire
30/11/2012, B, Flood
14/03/2013, B, Fire'''

df = pd.read_csv(StringIO(s), sep=',\s+', engine='python')

# Ignore everything above this part, it's simply creating your dataframe.

areas = df[df['NaturalDisaster']=='Fire'].groupby('Area')['NaturalDisaster'].count() 
areas /= sum(areas)
areas.plot(kind='bar')

plt.show()