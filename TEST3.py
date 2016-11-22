import itertools
import string


def crack_dict(max, min=1, chars=None):
    assert max >= min >= 1

    if chars is None:
        import string
        chars = string.printable[:-5]

    p = []
    for i in range(min, max + 1):
        p.append(itertools.product(string.printable[:-5], repeat=i))

    return itertools.chain(*p)


# 测试一下：
max, min = 11, 11
d = crack_dict(max, min)

# print(sum([95 ** i for i in range(min, max + 1)]))
# print(type(d))
j = 0
for i in d:
    j += 1
    if ''.join(tuple(i))=='admin520520':
        print(''.join(tuple(i)), j)



