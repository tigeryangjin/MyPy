import numpy as np

cnt = 100
bit = 9
result_any = np.empty((cnt))
result_all = np.empty((cnt))
for i in range(cnt):
    arr = np.random.randn(bit)
    boo = (arr > 0)
    result_all[i] = boo.all()
    result_any[i] = boo.any()

print('all is True:', (result_all == 1).sum() / cnt)
print('any is True:', (result_any == 1).sum() / cnt)
