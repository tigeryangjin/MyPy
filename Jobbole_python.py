import requests
from numpy import genfromtxt, zeros
from pylab import plot, show, figure, subplot, hist, xlim, show

# 下载数据
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
u = requests.get(url)
localFile = open('iris.csv', 'w')
localFile.write(u.text)
localFile.close()

# 加载数据
# read the first 4 columns
data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# read the fifth column
target = genfromtxt('iris.csv', delimiter=',', usecols=([4]), dtype=str)

# print(data.shape)
# print(target.shape)
# print(set(target))
print(data[:, 0])
print(max(data[:, 0]))

# 图表展示
plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
# show()

xmin = min(data[:, 0])
xmax = max(data[:, 0])
figure()  # 创建绘图对象
# subplot(numRows, numCols, plotNum):
# subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号
# xlim:设置x坐标轴的范围
subplot(411)  # distribution of the setosa class (1st, on the top)
hist(data[target == 'setosa', 0], color='b', alpha=.7)
xlim(xmin, xmax)
subplot(412)  # distribution of the versicolor class (2nd)
hist(data[target == 'versicolor', 0], color='r', alpha=.7)
xlim(xmin, xmax)
subplot(413)  # distribution of the virginica class (3rd)
hist(data[target == 'virginica', 0], color='g', alpha=.7)
xlim(xmin, xmax)
subplot(414)  # global histogram (4th, on the bottom)
hist(data[:, 0], color='y', alpha=.7)
xlim(xmin, xmax)
# show()
