myDat = [
    [1, 0, 1, 'yes'],
    [1, 1, 1, 'yes'],
    [1, 0, 0, 'no'],
    [0, 1, 1, 'no'],
    [0, 0, 1, 'no'],
]


def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]
            reducedFeatVec.extend(featVec[axis + 1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet


print(splitDataSet(myDat, 0, 0))
print(splitDataSet(myDat, 0, 1))
print(splitDataSet(myDat, 1, 0))
print(splitDataSet(myDat, 1, 1))
print(splitDataSet(myDat, 2, 0))
print(splitDataSet(myDat, 2, 1))

ll=[]
print('---------------------------------------------------')
for i in myDat:
    print(i)
    print(i[:0])
    print(i[1:])
print('---------------------------------------------------')
for j in myDat:
    print(j)
    print(j[:1])
    print(j[2:])
    l=j[:1]
    l.extend(j[2:])
    ll.append(l)
    print(ll)
print('---------------------------------------------------')
for k in myDat:
    print(k)
    print(k[:2])
    print(k[3:])
