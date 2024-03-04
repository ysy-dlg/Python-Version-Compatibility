import pandas as pd
import numpy as np

N = 100
df = pd.DataFrame(
    {'date': pd.date_range('2000-1-1', periods=N, freq='H'),
     'value': np.random.random(N)})

index = pd.DatetimeIndex(df['date'])
df.iloc[index.indexer_between_time('8:00','21:00')]