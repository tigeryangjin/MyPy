from numpy import *
# from numpy import array
import matplotlib
import matplotlib.pyplot as plt

a = random.random(size=50)
b = random.random(size=50)

x = array([a, b])

# print(x)
# basic
f1 = plt.figure(1)
plt.subplot(211)
plt.scatter(x[:, 1], x[:, 0])

# with label
plt.subplot(212)
label = list(ones(20)) + list(2 * ones(15)) + list(3 * ones(15))
label = array(label)

# plt.scatter(x[:, 1], x[:, 0], 15.0 * label, 15.0 * label)
print(x)
print(x[:, 0])
print(x[:, 1])
print(label)
