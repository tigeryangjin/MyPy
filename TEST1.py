import itertools
import string


def crackdict(max, min=1, chars=None):
    assert max >= min >= 1

    if chars is None:
        # import string
        chars = string.printable[:-5]

    p = []
    for i in range(min, max + 1):
        p.append(itertools.product(string.printable[:-5], repeat=i))

    return itertools.chain(*p)


# 测试一下：
max, min = 4, 1
d = crackdict(max, min)

print(sum((1 for i in d)))

print(sum([95 ** i for i in range(min, max + 1)]))
