import itertools


def crack_dict(max_len, min_len=1, chars=None):
    assert max_len >= min_len >= 1

    if chars is None:
        import string
        chars = string.printable[:-5]

    p = []
    for i in range(min_len, max_len + 1):
        p.append(itertools.product(chars, repeat=i))

    return itertools.chain(*p)



# 测试一下：
a, b = 11, 11
d = crack_dict(a, b)

# print(sum([95 ** i for i in range(min, max + 1)]))
# print(type(d))
j = 0
for k in d:
    j += 1
    if ''.join(tuple(k)) == 'admin520520':
        print(''.join(tuple(k)), j)
