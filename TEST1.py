import numpy as np

a=(5800,135)
print(type(a))
b=[5800,135]
print(type(b))
c={5800,135}
print(type(c))

d=np.array(b).reshape(1,-1)
print(type(d))

e=np.array(b).reshape(-1,1)
print(e)
print(type(e))