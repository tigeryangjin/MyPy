import random



n = 20
list_id = []
for i in range(n):
    list_id.append(i + 1)
print(list_id)
while len(list_id) > 1:
    live_count = len(list_id)
    r = random.randrange(1, live_count+1, 2)
    list_id.pop(r - 1)
    print('live_count:',live_count)
    print('r:',r)
    print(list_id)

