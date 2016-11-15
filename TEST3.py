import random


def px(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def alltime(list):
    alllist = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i == j:
                pass
            else:
                for k in range(len(list)):
                    if k == i or k == j:
                        pass
                    else:
                        for l in range(len(list)):
                            if l == j or l == j or l == k:
                                pass
                            else:
                                alllist.append(str(list[i]) + str(list[j]) + str(list[k]) + str(list[l]))
    return alllist


a = []
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
print(a)
a = px(a)
print(a)
print(alltime(a))
