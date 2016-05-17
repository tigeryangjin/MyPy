import random
import matplotlib.pyplot as plt

allx1 = []
ally1 = []
allx2 = []
ally2 = []
allx3 = []
ally3 = []
allx4 = []
ally4 = []
x_one = []
y_one = []
x_two = []
y_two = []
x_three = []
y_three = []
x_four = []
y_four = []
for row in range(5000):
    x1 = -random.random()
    y1 = random.random()
    x2 = random.random()
    y2 = random.random()
    x3 = -random.random()
    y3 = -random.random()
    x4 = random.random()
    y4 = -random.random()
    allx1.append([x1])
    ally1.append([y1])
    allx2.append([x2])
    ally2.append([y2])
    allx3.append([x3])
    ally3.append([y3])
    allx4.append([x4])
    ally4.append([y4])
    if x1 ** 2 + y1 ** 2 <= 1:
        x_one.append([x1])
        y_one.append([y1])
    if x2 ** 2 + y2 ** 2 <= 1:
        x_two.append([x2])
        y_two.append([y2])
    if x3 ** 2 + y3 ** 2 <= 1:
        x_three.append([x3])
        y_three.append([y3])
    if x4 ** 2 + y4 ** 2 <= 1:
        x_four.append([x4])
        y_four.append([y4])


# 画图，全部点用蓝色表示，圆内的点用红色表示
plt.scatter(allx1, ally1, color='w')
plt.scatter(allx2, ally2, color='g')
plt.scatter(allx3, ally3, color='k')
plt.scatter(allx4, ally4, color='m')
plt.scatter(x_one, y_one, color='r')
plt.scatter(x_two, y_two, color='b')
plt.scatter(x_three, y_three, color='y')
plt.scatter(x_four, y_four, color='c')
plt.show()
