from numpy import genfromtxt
from pylab import plot, show

# 加载数据
# read the first 4 columns
data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# read the fifth column
target = genfromtxt('iris.csv', delimiter=',', usecols=([4]), dtype=str)

print(type(data))
print(type(target))

# 图表展示
plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
show()
