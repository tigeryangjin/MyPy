import math

PRIME_LIST = []


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
    global PRIME_LIST
    num = 1
    while num >= 1:
        if is_prime(num) is True:
            PRIME_LIST.append(num)
        num += 2
        if num >= math.sqrt(x):
            break
    return PRIME_LIST


def prime_factorization(m):
    # 整数(m)分解成二个素数（p,q）的乘积
    # 988027
    prime(int(math.sqrt(m)))
    for i in range(len(PRIME_LIST)):
        if m / PRIME_LIST[i] == int(m / PRIME_LIST[i]):
            return m, m / PRIME_LIST


print(prime_factorization(988027))
print(PRIME_LIST)
print(int(math.sqrt(988027)))
