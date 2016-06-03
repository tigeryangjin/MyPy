# pylab
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm

img = pd.read_csv('d:\\kaggle\\digit-recognizer\\test.csv')

for k in range(4, 7):
    p1 = img.values[k]
    pix = []
    for i in range(28):
        pix.append([])
        for j in range(28):
            pix[i].append(p1[i * 28 + j])
    plt.imshow(pix, cmap=cm.get_cmap('gray_r'))
    plt.show()
