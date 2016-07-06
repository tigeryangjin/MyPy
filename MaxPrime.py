import math


def is_prime(x):
    # 判断x是否为素数，如果是素数则返回True，否则返回False
    if x <= 1:
        return False
    if x >= 2:
        i = 2
        while i * i <= x:
            if x % i == 0:
                return False
            i += 1
        return True


def prime(x):
    # 返回素数列表prime_list
    prime_list = []
    num = 1
    while num >= 1:
        if is_prime(num) is True:
            prime_list.append(num)
        num += 2
        if num >= x:
            break
    return prime_list


def factoring(x):
    prime_list = prime(x)
    for i in range(len(prime_list)):
        m = x / prime_list[i]
        if m / int(m) == 1:
            return int(x), int(prime_list[i]), int(x / m)


print(is_prime(9967))
print(prime(10000))
# print(factoring(280123))
