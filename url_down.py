import urllib.request
from pylab import figure, subplot, hist, xlim, plot, show
from numpy import genfromtxt

# 从网络上抓取CSV文件保存到本地磁盘
url = urllib.request.urlopen('http://aima.cs.berkeley.edu/data/iris.csv')
my_data = url.read().decode("utf8")
url.close()
file_object = open('G:\\Documents\\Python_tmp\\iris.csv', 'w')
file_object.write(my_data)
file_object.close()

# read the first 4 columns
data = genfromtxt('G:\\Documents\\Python_tmp\\iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# read the fifth column
target = genfromtxt('G:\\Documents\\Python_tmp\\iris.csv', delimiter=',', usecols=(4), dtype=str)

# 散点图
plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
show()

# 直方图
xmin = min(data[:, 0])
xmax = max(data[:, 0])
figure()
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
show()
