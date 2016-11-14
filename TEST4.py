import copy

tempList = [0, 1, 2, [3, 4]]
testList = tempList
testCopyList = copy.copy(tempList)
testDeepCopyList = copy.deepcopy(testList)

tempList.append('sign1')
print(testList)
print(testCopyList)
print(testDeepCopyList)

testList[3].append('sign2')
print(testList)
print(testCopyList)
print(testDeepCopyList)
