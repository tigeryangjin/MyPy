from sklearn.linear_model import LinearRegression
from sklearn.cross_validation import KFold
import pandas
import numpy as np

titanic = pandas.read_csv("F:\Documents\MyPy\MyPy\kaggle_titanic\Data\\train.csv")

# Age列缺失值使用均值填充
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].median())
# Sex列字符类型转换数字类型
titanic.loc[titanic['Sex'] == 'male', 'Sex'] = 0
titanic.loc[titanic['Sex'] == 'female', 'Sex'] = 1

titanic['Embarked'] = titanic['Embarked'].fillna('S')
titanic.loc[titanic['Embarked'] == 'S', 'Embarked'] = 0
titanic.loc[titanic['Embarked'] == 'C', 'Embarked'] = 1
titanic.loc[titanic['Embarked'] == 'Q', 'Embarked'] = 2
# The columns we'll use to predict the target
predictors = ['Pclass', 'Sex', 'Age', 'SibSp', 'Parch', 'Fare', 'Embarked']

# Initialize our algorithm class
alg = LinearRegression()

kf = KFold(titanic.shape[0], n_folds=3, random_state=1)

predictions = []
for train, test in kf:
    train_predictors = (titanic[predictors].iloc[train, :])
    train_target = titanic['Survived'].iloc[train]
    alg.fit(train_predictors, train_target)
    test_predictions = alg.predict(titanic[predictors].iloc[test, :])
    predictions.append(test_predictions)

predictions = np.concatenate(predictions, axis=0)
predictions[predictions > .5] = 1
predictions[predictions <= .5] = 0
accuracy = sum(predictions[predictions == titanic['Survived']]) / len(predictions)
print(accuracy)
print(titanic['Survived'].describe())
