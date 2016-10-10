import math
import time

PRIME_LIST = []


def is_prime(x):
    # 判断x是否为素数，如果是素数则返回True，否则返回False
    if x <= 1:
        return False
    if x >= 2:
        i = 2
        while i * i <= x:
            # s = math.sqrt(x)
            # while i <= s:
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
            PRIME_LIST.append(num)
        num += 2
        if num >= math.sqrt(x):
            break
    return PRIME_LIST


def prime_factorization(m):
    # 整数(m)分解成二个素数（p,q）的乘积
    # 991*997=988027
    prime_list(m)
    for i in range(len(PRIME_LIST)):
        p = PRIME_LIST[i]
        q = m / p
        if q == int(q):
            return p, int(q)
            # return m, int(m / PRIME_LIST)


def prime_f2(m):
    s = int(math.sqrt(m))
    for i in range(s):
        if is_prime(i) is True:
            p = i
            q = m / p
            if q == int(q):
                return p, int(q)


# p = 47066161
# q = 43258601
p = 974411
q = 638621
m = p * q
print(p, is_prime(p))
print(q, is_prime(q))
print(p * q)
start = time.clock()
print(prime_factorization(m))
elapsed = time.clock() - start
print("Time used:", elapsed)
start2 = time.clock()
print(prime_f2(m))
elapsed2 = time.clock() - start2
print("Time used:", elapsed2)
