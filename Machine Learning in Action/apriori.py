def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    C1=[]
    for transaction in dataSet:
        for item in transaction:
            if not [item] in C1:
                C1. append([ item])
    C1. sort() #❶ 对 C1 中 每个 项 构建 一个 不变 集合
    return map( frozenset, C1)

print(loadDataSet())


