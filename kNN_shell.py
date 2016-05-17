import matplotlib
import matplotlib.pyplot as plt
import kNN
from numpy import *
datingDataMat,datingLabels=kNN.file2matrix('E:/Personal/BOOK/机器学习/机器学习实战源代码/machinelearninginaction/Ch02/datingTestSet2.txt')
fig=plt.figure()
ax=fig.add_subplot(111)
ax.scatter(datingDataMat[:,1],datingDataMat[:,2],15.0*array(datingLabels),15.0*array(datingLabels))
#plt.show()
#print(datingDataMat)

norMat,ranges,minVals=kNN.autoNorm(datingDataMat)
#print(norMat)

kNN.datingClassTest()