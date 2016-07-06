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
        return x


def prime(x):
    # 返回素数列表prime_list
    # prime_list = []
    num = 1
    while num >= 1:
        if is_prime(num) == num:
            print(num)
        num += 2
    # return prime_list


print(prime(100))
