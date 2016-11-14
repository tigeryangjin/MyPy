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


def plt_scatter():
    datingDataMat, datingLabels = file2matrix(
        'E:\Personal\BOOK\机器学习\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    # 散点图
    fig = plt.figure()
    ax = fig.add_subplot(211)
    ax.scatter(datingDataMat[:, 0], datingDataMat[:, 1], 15 * array(datingLabels), 15 * array(datingLabels))
    ay = fig.add_subplot(212)
    ay.scatter(normMat[:, 0], normMat[:, 1], 15 * array(datingLabels), 15 * array(datingLabels))
    plt.show()


def datingClassTest():
    hoRatio = 0.10  # 10%记录作为测试集
    datingDataMat, datingLabels = file2matrix(
        'E:\Personal\BOOK\机器学习\MLiA_SourceCode\machinelearninginaction\Ch02\datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)  # 100条记录作为测试集
    errorCount = 0.0  # 错误记录计数器
    for i in range(numTestVecs):
        classifierResult = classify0(normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print('the classifier came back with: %d,the real answer is: %d' % (classifierResult, datingLabels[i]))
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print('the total error rate is: %f' % (errorCount / float(numTestVecs)))


datingClassTest()
plt_scatter()



