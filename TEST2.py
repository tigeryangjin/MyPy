import numpy as np
from pylab import plot, show

# 加载数据
da = np.fromfile('iris.csv')
print(da)
print(type(da))

# 图表展示
# plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
# plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
# plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
# show()
