import numpy as np

data = np.loadtxt('populations.txt')
np.savetxt('pop2.txt', data)
data2 = np.loadtxt('pop2.txt')
print(data2)
