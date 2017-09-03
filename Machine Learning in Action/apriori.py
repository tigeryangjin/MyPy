def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]


def createC1(dataSet):
    C1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1.append([item])
    C1.sort()  # 对C1中每个项构建一个不变集合
    return map(frozenset, C1)


def scanD(D, Ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in Ck:
            if can.issubset(tid):
                if not ssCnt.has_key(can):
                    ssCnt[can] = 1
                else:
                    ssCnt[can] += 1
    numItems = float(len(list(D)))
    retList = []
    supportData = {}
    for key in ssCnt:
        # 计算所有项集的支持度
        support = ssCnt[key] / numItems
        if support >= minSupport: retList.insert(0, key)
        supportData[key] = support
    return retList, supportData


dataSet = loadDataSet()
C1 = createC1(dataSet)
print(list(C1))
D = map(set, dataSet)
print(list(D))
L1, suppData0 = scanD(D, C1, 0.5)
print(L1)
