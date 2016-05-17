from numpy import *

fr = open('E:/Personal/BOOK/机器学习/机器学习实战源代码/machinelearninginaction/Ch02/datingTestSet.txt')
dic = {'didntLike': '1', 'smallDoses': '2', 'largeDoses': '3'}
tranDataSet=zeros((1000,3))
index=0
levelList=[]
for line in fr.readlines():
    line=line.strip()
    line=line.split('\t')
    tranDataSet[index:]=line[0:3]
    levelList.append(dic[line[3]])
    index+=1
levelMatrx=matrix(levelList)
dataMatrix=matrix(tranDataSet)

print(dataMatrix)
print(levelMatrx)





