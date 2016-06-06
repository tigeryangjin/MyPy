def linear_regression(x, y):
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    a = 0
    b = 0
    c = 0
    for i in range(len(x)):
        a += (x[i] - x_mean) * (y[i] - y_mean)
        # print('a: ', a)
        b += (x[i] - x_mean) ** 2
        # print('b: ', b)
        c += (y[i] - y_mean) ** 2
        # print('c: ', c)
    r = a / ((b * c) ** 0.5)
    return r


x = [1, 2]
y = [1, 2]

print(linear_regression(x, y))
