import random

a = []
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))

print(a)
for i in range(3):
    for j in range(3):
        if i == j:
            pass
        else:
            for k in range(3):
                if j == k or i == k:
                    pass
                else:
                    print(a[i], a[j], a[k])
