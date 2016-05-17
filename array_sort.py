from numpy import *


def array_sort(arrayinput):
    index = argsort(arrayinput)
    arraysort = arrayinput
    arrayout = []
    for i in range(len(arrayinput)):
        d = arraysort[index[i]]
        arrayout.append(d)
    return arrayout
