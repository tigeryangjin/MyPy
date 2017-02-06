import random


def live():
    # 总人数
    n = 600
    list_id = []
    for i in range(n):
        list_id.append(i + 1)

    while len(list_id) > 1:
        live_count = len(list_id)
        r = random.randrange(1, live_count + 1, 2)
        # 抽中的人出列
        list_id.pop(r - 1)
    # 返回最后活下来的
    return list_id

for i in range(10000):
    last_live_id=[]
    last_live_id.append(live())
