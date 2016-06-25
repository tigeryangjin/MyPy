import time
from time import gmtime, strftime

# now = time.localtime()
# print(now)
# print(strftime("%a, %d %b %Y %H:%M:%S +0000", now))

n=time.ctime()
print(n)
print(time.strptime(n))

