import random

a = []
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))
a.append(random.randint(0, 9))


def order(list):
    # 倒序排列四位数字
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list


def find_max(list):
    # time_list存放所有的合法时间，并且从小到大排列
    time_list = []
    for i in range(len(list)):
        for j in range(len(list)):
            if j == i:
                pass
            else:
                for k in range(len(list)):
                    if k == i or k == j:
                        pass
                    else:
                        for l in range(len(list)):
                            if l == i or l == j or l == k:
                                pass
                            else:
                                if list[i] <= 2 and list[j] <= 3 and list[k] <= 5:
                                    time_list.append(str(list[i]) + str(list[j]) + ':' + str(list[k]) + str(list[l]))
    if len(time_list) == 0:
        max_time_str = 'no time!'
    else:
        max_time_str = time_list[-1]
    return max_time_str


print(a)
a = order(a)
print(find_max(a))
