from scipy.ndimage.filters import maximum_filter1d
df['max'] = maximum_filter1d(df.High,size=3,origin=1,mode='nearest')