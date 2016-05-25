def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


def is_int(x):
    if x % 1 == 0:
        return True
    else:
        return False


def digit_sum(n):
    m = 0
    for i in str(n):
        m += int(i)
    return m


def factorial(x):
    if x == 0:
        return 1
    else:
        f = 1
        for i in range(1, x + 1):
            f *= i
        return f


def is_prime(x):
    if x <= 1:
        return False
    if x >= 2:
        i = 2
        while i <= x - 1:
            if x % i == 0:
                return False
            i += 1
        return True


def reverse(str):
    listStr = []
    revStr = []
    for i in str:
        listStr.append(i)

    for i in range(len(listStr)):
        revStr.append(listStr[len(listStr) - i - 1])
    return ''.join(revStr)


def anti_vowel(text):
    vowel = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    textNoVowel = []
    for i in text:
        if i not in vowel:
            textNoVowel.append(i)
    return ''.join(textNoVowel)


def scrabble_score(word):
    score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1,
             "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10,
             "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
             "x": 8, "z": 10}
    sumScore = 0
    lowerWord = word.lower()
    for i in lowerWord:
        sumScore += score[i]
    return sumScore


def censor(text, word):
    str = '*' * len(word)
    listText = text.split()
    listWord = word.split()
    for i in range(len(listText)):
        if listText[i] in listWord:
            listText[i] = str
    return ' '.join(listText)


def count(sequence, item):
    countItem = 0
    for i in sequence:
        if i == item:
            countItem += 1
        else:
            countItem = countItem
    return countItem


def purify(listNum):
    listEven = []
    for i in listNum:
        if i % 2 == 0:
            listEven.append(i)
    return listEven


def product(listNum):
    mul = 1
    for i in listNum:
        mul *= i
    return mul


def remove_duplicates(listDup):
    listReturn = []
    for i in listDup:
        if i not in listReturn:
            listReturn.append(i)
    return listReturn


def median(listIn):
    listSort = sorted(listIn)
    listLen = len(listSort)
    if listLen % 2 == 0:
        medianEven = (float(listSort[int(listLen / 2)]) + float(listSort[int(listLen / 2 - 1)])) / 2
        return medianEven
    else:
        medianOdd = listSort[int(listLen / 2)]
        return medianOdd


print(median([4, 5, 5, 4]))
