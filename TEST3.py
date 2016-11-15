for i in range(4):
    for j in range(4):
        if i == j:
            pass
        else:
            for k in range(4):
                if k == i or k == j:
                    pass
                else:
                    for l in range(4):
                        if l == i or l == j or l == k:
                            pass
                        else:
                            print(str(i) + str(j) + str(k) + str(l))
