import numpy as np

a = np.arange(0, 12)
a.shape = 3, 4
a.tofile('a.bin')
b = np.fromfile('a.bin', dtype=np.int32)
print(b)
b.shape = 3, 4
print(b)
