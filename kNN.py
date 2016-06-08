from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt


def createDataSet():
    group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
    labels = ['A', 'A', 'B', 'B']
    return group, labels


def classify0(inX, dataSet, labels, k):
    dataSetSize = dataSet.shape[0]
    diffMat = tile(inX, (dataSetSize, 1)) - dataSet
    sqDiffMat = diffMat ** 2
    sqDistances = sqDiffMat.sum(axis=1)
    distances = sqDistances ** 0.5
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]


# group, labels = createDataSet()
# print(classify0([0, 0], group, labels, 3))

def file2matrix(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())  # get the number of lines in the file
    returnMat = zeros((numberOfLines, 3))  # prepare matrix to return
    classLabelVector = []
    fr = open(filename)
    index = 0
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split('\t')
        returnMat[index, :] = listFromLine[0:3]
        classLabelVector.append(int(listFromLine[-1]))
        index += 1
    return returnMat, classLabelVector


def autoNorm(dataSet):
    # newValue=(oldValue-min)/(max-min)
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


datingDataMat, datingLabels = file2matrix(
    'E:\Personal\BOOK\机器学习\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
# print(datingDataMat)
print(datingDataMat - tile(datingDataMat.min(0), (1000, 1)))
# print(datingLabels)

# 散点图
fig = plt.figure()
ax = fig.add_subplot(131)
# c='r':颜色为红色
ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2], c='r')
ay = fig.add_subplot(132)
ay.scatter(datingDataMat[:, 1], datingDataMat[:, 2], 15 * array(datingLabels), 15 * array(datingLabels))
az = fig.add_subplot(133)
az.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15 * array(datingLabels), 15 * array(datingLabels))
# plt.show()
