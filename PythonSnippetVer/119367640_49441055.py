import pandas as pd
import numpy as np

data = '''\
ID   Name     2018-02-28    2018-01-31    2018-12-31    2017-11-30    2017-10-31    2017-09-30
11   ABC      110           109           108             100            95                90
22   DEF      120           119           118             100            85                80
33   GHI      130           129           128             100            75                70'''

df = pd.read_csv(pd.compat.StringIO(data), sep='\s+').set_index('ID')
