from numpy import *
# from numpy import array
import matplotlib
import matplotlib.pyplot as plt

a = random.randint(0, 50, 50)
b = random.randint(0, 50, 50)


f1 = plt.figure(1)
plt.subplot(211)
plt.scatter(a, b)

# with label
plt.subplot(212)
label = list(ones(20)) + list(2 * ones(15)) + list(3 * ones(15))
label = array(label)

plt.scatter(a, b, 15.0 * label, 15.0 * label)
plt.show()

print(a)
print(b)
print(label)
