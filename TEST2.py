def is_prime(x):
    # 判断x是否为素数，如果是素数则返回True，否则返回False
    if x <= 1:
        return False
    if x >= 2:
        i = 2
        while i * i <= x:
            if i % 2 == 0:
                i += 1
                print(i)
            elif i % 3 == 0:
                i += 1
                print(i)
            elif i % 5 == 0:
                i += 1
                print(i)
            elif i % 7 == 0:
                i += 1
                print(i)
            elif i % 11 == 0:
                i += 1
                print(i)
            elif i % 13 == 0:
                i += 1
                print(i)
            elif i % 17 == 0:
                i += 1
                print(i)
            else:
                if x % i == 0:
                    return False
                i += 2
                print(i)
        return True


print(is_prime(131071))
