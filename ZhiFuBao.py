# 支付宝2.15亿奖金平分
def zfb(min_person, max_person, total_amt):
    import matplotlib.pyplot as plt
    ind = []
    dif = []
    for p in range(min_person, max_person):
        ind.append(p)
        dif_amt = round(p * (total_amt / p - round(total_amt / p,2)),2)
        dif.append(dif_amt)
    for i in range(max_person-min_person):
        print(ind[i], dif[i])
    plt.scatter(ind, dif)
    plt.show()


zfb(1000, 3000, 20000)
