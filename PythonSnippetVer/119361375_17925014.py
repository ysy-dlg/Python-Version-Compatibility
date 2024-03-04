
import numpy as np
from scipy import stats
import scipy
print scipy.__version__
## Generate some random two-dimensional data:
def measure(n):
    m1 = np.random.normal(size=n)
    m2 = np.random.normal(scale=0.5, size=n)
    return m1+m2, m1-m2
m1, m2 = measure(2000)
xmin = m1.min()
xmax = m1.max()
ymin = m2.min()
ymax = m2.max()
# Perform a kernel density estimate on the data:
x, y = np.mgrid[xmin:xmax:100j, ymin:ymax:100j]
positions = np.vstack([x.ravel(), y.ravel()])
values = np.vstack([m1, m2])
kernel = stats.gaussian_kde(values)
kernel.silverman_factor()