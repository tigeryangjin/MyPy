import random

a = []
a.append(random.randint)
a.append(random.randint)
a.append(random.randint)
a.append(random.randint)
print(a)
print(random.randint)

def px(a, b):
    if a < b:
        a, b = b, a
    else:
        a, b = a, b
    return a, b


print(px(3, 5))
