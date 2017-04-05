import operator

dic = {'a': 3, 'b': 4, 'c': 5}
for k, v in dic.items():
    print("dic[%s]=" % k, v)
print(dic.items())
print(sorted(dic.items(), key=operator.itemgetter(0), reverse=True))
print(sorted(dic.items(), key=operator.itemgetter(0), reverse=False))
print(operator.itemgetter(1))
