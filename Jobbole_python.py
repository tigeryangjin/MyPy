import requests
from numpy import genfromtxt, zeros, array
from pylab import plot, figure, subplot, hist, xlim, show
from matplotlib import pyplot as plt
from sklearn.naive_bayes import GaussianNB
from sklearn import cross_validation
from sklearn.metrics import classification_report


def download_data():
    # 下载数据
    url = 'http://aima.cs.berkeley.edu/data/iris.csv'
    u = requests.get(url)
    local_file = open('iris.csv', 'w')
    local_file.write(u.text)
    local_file.close()


# 加载数据
# 全局变量
# read the first 4 columns
# 如果此处用loadtxt会有问题。
data = genfromtxt('iris.csv', delimiter=',', usecols=(0, 1, 2, 3))
# read the fifth column
target = genfromtxt('iris.csv', delimiter=',', usecols=([4]), dtype=str)


# print(type(data))
# print(type(target))

def fig1():
    # 图表展示
    plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
    plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
    plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
    plt.title('jdkjs')
    show()


# fig1()


def fig2():
    # 花萼长度--------------------------------------------------------
    xmin = min(data[:, 0])
    xmax = max(data[:, 0])
    figure()  # 创建绘图对象
    # subplot(numRows, numCols, plotNum):
    # subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号
    # xlim:设置x坐标轴的范围
    subplot(441)  # distribution of the setosa class (1st, on the top)
    hist(data[target == 'setosa', 0], color='b', alpha=.7)
    plt.title('setosa|sepal|L')
    xlim(xmin, xmax)
    subplot(442)  # distribution of the versicolor class (2nd)
    hist(data[target == 'versicolor', 0], color='r', alpha=.7)
    plt.title('versicolor|sepal|L')
    xlim(xmin, xmax)
    subplot(443)  # distribution of the virginica class (3rd)
    hist(data[target == 'virginica', 0], color='g', alpha=.7)
    plt.title('virginica|sepal|L')
    xlim(xmin, xmax)
    subplot(444)  # global histogram (4th, on the bottom)
    hist(data[:, 0], color='y', alpha=.7)
    plt.title('Avg|sepal|L')
    xlim(xmin, xmax)
    # show()

    # 花萼宽度--------------------------------------------------------
    xmin = min(data[:, 1])
    xmax = max(data[:, 1])
    # figure()  # 创建绘图对象
    # subplot(numRows, numCols, plotNum):
    # subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号
    # xlim:设置x坐标轴的范围
    subplot(445)  # distribution of the setosa class (1st, on the top)
    hist(data[target == 'setosa', 1], color='b', alpha=.7)
    plt.title('setosa|sepal|W')
    xlim(xmin, xmax)
    subplot(446)  # distribution of the versicolor class (2nd)
    hist(data[target == 'versicolor', 1], color='r', alpha=.7)
    plt.title('versicolor|sepal|W')
    xlim(xmin, xmax)
    subplot(447)  # distribution of the virginica class (3rd)
    hist(data[target == 'virginica', 1], color='g', alpha=.7)
    plt.title('virginica|sepal|W')
    xlim(xmin, xmax)
    subplot(448)  # global histogram (4th, on the bottom)
    hist(data[:, 1], color='y', alpha=.7)
    plt.title('Avg|sepal|W')
    xlim(xmin, xmax)
    # show()

    # 花瓣长度--------------------------------------------------------
    xmin = min(data[:, 2])
    xmax = max(data[:, 2])
    # figure()  # 创建绘图对象
    # subplot(numRows, numCols, plotNum):
    # subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号
    # xlim:设置x坐标轴的范围
    subplot(449)  # distribution of the setosa class (1st, on the top)
    hist(data[target == 'setosa', 2], color='b', alpha=.7)
    plt.title('setosa|petal|L')
    xlim(xmin, xmax)
    subplot(4, 4, 10)  # distribution of the versicolor class (2nd)
    hist(data[target == 'versicolor', 2], color='r', alpha=.7)
    plt.title('versicolor|petal|L')
    xlim(xmin, xmax)
    subplot(4, 4, 11)  # distribution of the virginica class (3rd)
    hist(data[target == 'virginica', 0], color='g', alpha=.7)
    plt.title('virginica|petal|L')
    xlim(xmin, xmax)
    subplot(4, 4, 12)  # global histogram (4th, on the bottom)
    hist(data[:, 2], color='y', alpha=.7)
    plt.title('Avg|petal|L')
    xlim(xmin, xmax)
    # show()

    # 花瓣宽度--------------------------------------------------------
    xmin = min(data[:, 3])
    xmax = max(data[:, 3])
    # figure()  # 创建绘图对象
    # subplot(numRows, numCols, plotNum):
    # subplot将整个绘图区域等分为numRows行 * numCols列个子区域，然后按照从左到右，从上到下的顺序对每个子区域进行编号
    # xlim:设置x坐标轴的范围
    subplot(4, 4, 13)  # distribution of the setosa class (1st, on the top)
    hist(data[target == 'setosa', 3], color='b', alpha=.7)
    plt.title('setosa|petal|W')
    xlim(xmin, xmax)
    subplot(4, 4, 14)  # distribution of the versicolor class (2nd)
    hist(data[target == 'versicolor', 3], color='r', alpha=.7)
    plt.title('versicolor|petal|W')
    xlim(xmin, xmax)
    subplot(4, 4, 15)  # distribution of the virginica class (3rd)
    hist(data[target == 'virginica', 3], color='g', alpha=.7)
    plt.title('virginica|petal|W')
    xlim(xmin, xmax)
    subplot(4, 4, 16)  # global histogram (4th, on the bottom)
    hist(data[:, 3], color='y', alpha=.7)
    plt.title('Avg|petal|W')
    xlim(xmin, xmax)
    show()


# fig2()

# 分类
def clsfr():
    train1_err = []
    # test1_err = []
    train2_err = []
    test2_err = []
    t = zeros(len(target))
    t[target == 'setosa'] = 1
    t[target == 'versicolor'] = 2
    t[target == 'virginica'] = 3
    classifier = GaussianNB()
    classifier.fit(data, t)  # training on the iris dataset
    for i in range(len(t)):
        if classifier.predict(data[i]) != array(t[i]):
            train1_err.append((classifier.predict(data[i]), t[i]))
    train, test, t_train, t_test = cross_validation.train_test_split(data, t, test_size=0.4, random_state=0)
    classifier.fit(train, t_train)  # train
    for i in range(len(t_train)):
        if classifier.predict(train[i]) != array(t_train[i]):
            train2_err.append((classifier.predict(train[i]), t_train[i]))
    for i in range(len(t_test)):
        if classifier.predict(test[i]) != array(t_test[i]):
            test2_err.append((classifier.predict(test[i]), t_test[i]))
    print('train error: ', train1_err)
    print('train count: ', len(t))
    print('train error count: ', len(train1_err))
    print('accuracy rate: ', classifier.score(data, t))
    print('*******************************************')
    print('train error: ', train2_err)
    print('test error: ', test2_err)
    print('train count: ', len(train))
    print('train error count: ', len(train2_err))
    print('test count: ', len(test))
    print('test error count: ', len(test2_err))
    print('test accuracy rate: ', classifier.score(test, t_test))  # test
    print('train accuracy rate: ', classifier.score(train, t_train))
    print('****************************************************')
    print(classification_report(classifier.predict(test), t_test, target_names=['setosa', 'versicolor', 'virginica']))


# 聚类
def cluster():
    from sklearn.cluster import KMeans
    from sklearn.metrics import completeness_score, homogeneity_score
    kmeans = KMeans(n_clusters=3, init='random')
    kmeans.fit(data)
    c = kmeans.predict(data)
    # print(completeness_score(target, c))  # 完整性得分，当大部分数据点属于一个给定的类并且属于同一个群集，那么完整性得分就趋向于1
    # print(homogeneity_score(target, c))  # 同质性得分，当所有群集都几乎只包含某个单一类的数据点时同质性得分就趋向于1
    figure()
    subplot(211)  # top figure with the real classes
    plot(data[target == 'setosa', 0], data[target == 'setosa', 2], 'bo')
    plot(data[target == 'versicolor', 0], data[target == 'versicolor', 2], 'ro')
    plot(data[target == 'virginica', 0], data[target == 'virginica', 2], 'go')
    print(c)
    print(target)
    print(type(c))
    print(type(target))
    print(data)
    print(type(data))
    subplot(212)  # bottom figure with classes assigned automatically
    plot(data[c == 0, 0], data[c == 0, 2], 'ro', alpha=.7)
    plot(data[c == 1, 0], data[c == 1, 2], 'go', alpha=.7)
    plot(data[c == 2, 0], data[c == 2, 2], 'bo', alpha=.7)
    show()


cluster()
