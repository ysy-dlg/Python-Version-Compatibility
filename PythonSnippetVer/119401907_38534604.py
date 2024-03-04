import numpy as np
import pandas as pd

# 1
t1 = df.sort_values(['store_code', 'week_hr'])
# 2
t2 = t1[t1['baskets'] == 0]
# 3
continuous = t2['week_hr'][1:].values-t2['week_hr'][:-1].values == 1
groups = np.cumsum(np.hstack([False, continuous==False]))
t2['groups'] = groups
# 4
t3 = t2.groupby(['store_code', 'groups'], as_index=False)['week_hr'].count()
t4 = t3[t3.week_hr > 2]
print pd.merge(t2, t4[['store_code', 'groups']])