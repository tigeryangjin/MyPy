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
        if num >= math.sqrt(x):
            break
    return prime_list


def prime_factorization():
    # 整数(m)分解成二个素数（p,q）的乘积

    pass
