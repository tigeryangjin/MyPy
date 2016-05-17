from numpy import genfromtxt

data = genfromtxt('G:\\Documents\\Python_tmp\\iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
target = genfromtxt('G:\\Documents\\Python_tmp\\iris.csv', dtype=str, delimiter=',', usecols=(4))
print(target)