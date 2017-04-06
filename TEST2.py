trainMat = []
listOPosts = [[' my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
              ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
              ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
              ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
              ['mr', 'licks', 'ate', 'my', 'steak', 'how', ' to', 'stop', 'him'],
              ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
myVocabList = ['take', 'dog', 'mr', 'please', ' to', 'stop', 'food', 'has', ' my', 'problems', 'to', 'ate', 'is',
               'quit',
               'stupid', 'him', 'my', 'flea', 'buying', 'so', 'maybe', 'garbage', 'posting', 'licks', 'cute', 'not',
               'help',
               'steak', 'how', 'park', 'love', 'dalmation', 'I', 'worthless']


def setOfWord2Vec(vocabList, inputSet):
    returnVec = [0] * len(vocabList)
    for word in inputSet:
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word: %s is not in my Vocabulary!' % word)
    return returnVec


for postinDoc in listOPosts:
    print(postinDoc)
    trainMat.append(setOfWord2Vec(myVocabList, postinDoc))

print(trainMat)
print(len(myVocabList))
