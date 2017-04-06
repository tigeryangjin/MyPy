from numpy import *

trainMat = [[1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1],
            [0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1, 0],
            [0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0]]
listClasses = [0, 1, 0, 1, 0, 1]
numWords = len(trainMat[0])
p0Num = zeros(numWords)
p1Num = zeros(numWords)
p0Denom = 0.0
p1Denom = 0.0
for i in range(len(trainMat)):
    if listClasses[i] == 1:
        p1Num += trainMat[i]
        p1Denom += sum(trainMat[i])
    else:
        p0Num += trainMat[i]
        p0Denom += sum(trainMat[i])
print('p0Num: ', p0Num)
print('p0Denom: ', p0Denom)
print('p0Num / p0Denom: ', p0Num / p0Denom)
print('p1Num: ', p1Num)
print('p1Denom: ', p1Denom)
print('p1Num / p1Denom: ', p1Num / p1Denom)
