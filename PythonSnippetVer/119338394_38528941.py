import numpy as np

array1 = [[1, 2, 3, 4, 5], [2, 4, 6, 8, 10], [3, 6, 9, 12, 15]]
array2 = [[6, 7, 8, 9, 10], [11, 22, 33, 44, 55], [1, 4, 9, 16, 25]]
array1, array2 = np.asarray(array1), np.asarray(array2)

diff = np.subtrat(array1, array2)
diff = np.absolute(diff)

print diff.max()
