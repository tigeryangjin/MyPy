import random


def live():
    n = 600
    list_id = []
    for i in range(n):
        list_id.append(i + 1)

    while len(list_id) > 1:
        live_count = len(list_id)
        r = random.randrange(1, live_count + 1, 2)
        list_id.pop(r - 1)
    return list_id


print(live())
