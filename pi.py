import random
import matplotlib.pyplot as plt

ax = []
ay = []
ix = []
iy = []
for row in range(10000):
    x = random.random()
    y = random.random()
    ax.append([x])
    ay.append([y])
    if x ** 2 + y ** 2 <= 1:
        ix.append([x])
        iy.append([y])
pi = len(ix) / len(ax) * 4
print('生成%s个点,其中%s个点在圆中，计算出pi=%s' % (len(ax), len(ix), pi))

# 画图，全部点用蓝色表示，圆内的点用红色表示
plt.scatter(ax, ay, color='b')
plt.scatter(ix, iy, color='r')
plt.show()

from pylab import plot, show

plt.plot(ax, ay, 'bo')
plt.plot(ix, iy, 'ro')
plt.show()
