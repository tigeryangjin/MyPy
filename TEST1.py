from time import time

t = time()
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listb = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.01]
for i in range(1000000):
    for a in range(len(lista)):
        for b in range(len(listb)):
            x = lista[a] + listb[b]
print("total run time:")
print(time() - t)
