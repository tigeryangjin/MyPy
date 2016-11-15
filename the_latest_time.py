import random


def px(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def alltime(list):
    alllist = []
    for i in range(0, len(list)):
        for j in range(1, len(list) - 1):
            for k in range(2, len(list) - 2):
                for l in range(3, len(list) - 3):
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
