dataSet = [
    [1, 1, 'yes'],
    [1, 1, 'yes'],
    [1, 0, 'no'],
    [0, 1, 'no'],
    [0, 1, 'no'],
]
retDataSet = []
# reducedFeatVec = []
axis = 0
for featVec in dataSet:
    # print(featVec[axis])
    # print(featVec[:axis])
    # print(featVec[axis + 1:])
    # reducedFeatVec = featVec[:axis]
    reducedFeatVec = []
    reducedFeatVec.extend(featVec[axis + 1:])
    retDataSet.append(reducedFeatVec)
print(retDataSet)
