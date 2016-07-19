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


def prime_list(x):
    # 返回素数列表prime_list
    global PRIME_LIST
    PRIME_LIST = []
    num = 1
    while num >= 1:
        if is_prime(num) is True:
            PRIME_LIST.append(int(num))
        num += 2
        if num >= math.sqrt(x):
            break
    return PRIME_LIST


def prime_factorization(m):
    # 整数(m)分解成二个素数（p,q）的乘积
    # 991*997=988027
    prime_list(int(m))
    for i in range(len(PRIME_LIST)):
        p = PRIME_LIST[i]
        q = m / p
        if q == int(q):
            return p, int(q)
            # return m, int(m / PRIME_LIST)


print(prime_factorization(1427247692705959880439315947500961989719490561))

