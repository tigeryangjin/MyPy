import matplotlib.pyplot as plt
# %matplotlib qt
# import numpy as np
import pandas as pd

# import statsmodels.api as sm
# from statsmodels.nonparametric.kde import KDEUnivariate
# from statsmodels.nonparametric import smoothers_lowess
# from pandas import DataFrame
# from patsy import dmatrices

df = pd.read_csv("G:/Documents/MyPython/kaggle_titanic/Data/train.csv")
df = df.drop(['Ticket', 'Cabin'], axis=1)  # 去除Ticket、Cabin列
df = df.dropna()  # 删除有数据缺失的行

# 指定图的参数
fig = plt.figure(figsize=(18, 6), dpi=100)
alpha = alpha_scatterplot = 0.2
alpha_bar_chart = 0.55

# 幸存数量对比
ax1 = plt.subplot2grid((2, 3), (0, 0))
# plots a bar graph of those who surived vs those who did not.
df.Survived.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
# this nicely sets the margins in matplotlib to deal with a recent bug 1.3.1
ax1.set_xlim(-1, 2)
# puts a title on our graph
plt.title("Distribution of Survival, (1 = Survived)")

# 年龄与幸存数量的关系对比
plt.subplot2grid((2, 3), (0, 1))
plt.scatter(df.Survived, df.Age, alpha=alpha_scatterplot)
# sets the y axis lable
plt.ylabel("Age")
# formats the grid line style of our graphs
plt.grid(b=True, which='major', axis='y')
plt.title("Survial by Age,  (1 = Survived)")

# 阶级与幸存数量的关系对比
ax3 = plt.subplot2grid((2, 3), (0, 2))
df.Pclass.value_counts().plot(kind="barh", alpha=alpha_bar_chart)
ax3.set_ylim(-1, len(df.Pclass.value_counts()))
plt.title("Class Distribution")

# 年龄与阶级
plt.subplot2grid((2, 3), (1, 0), colspan=2)
# plots a kernel desnsity estimate of the subset of the 1st class passanges's age
df.Age[df.Pclass == 1].plot(kind='kde')
df.Age[df.Pclass == 2].plot(kind='kde')
df.Age[df.Pclass == 3].plot(kind='kde')
# plots an axis lable
plt.xlabel("Age")
plt.title("Age Distribution within classes")
# sets our legend for our graph.
plt.legend(('1st Class', '2nd Class', '3rd Class'), loc='best')

# 登机位置与幸存数量的关系对比
ax5 = plt.subplot2grid((2, 3), (1, 2))
df.Embarked.value_counts().plot(kind='bar', alpha=alpha_bar_chart)
ax5.set_xlim(-1, len(df.Embarked.value_counts()))
# specifies the parameters of our graphs
plt.title("Passengers per boarding location")

plt.show()
