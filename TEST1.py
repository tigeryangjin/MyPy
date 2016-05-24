from numpy import genfromtxt, zeros, array

l = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'c', 'd']
a = array(l)
print(a)
x = zeros(10)
x[a == 'a'] = 1
print(type(x))
print(x)
