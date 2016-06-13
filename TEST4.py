import numpy as np

a = [[20, 5], [15, 10]]
a = np.asmatrix(a)
b = [[2, 1], [1, 4]]
b = np.mat(b)
print("matrix a:")
print(a)
print("matrix b:")
print(b)
c = a * b
print("matrix c:")
print(c)
