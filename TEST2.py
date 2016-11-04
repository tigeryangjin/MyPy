from sklearn.linear_model import LinearRegression

X = [[1, 1, 1], [1, 1, 2], [1, 2, 1]]
Y = [[6], [9], [8]]

model = LinearRegression()
model.fit(X, Y)
x2 = [[1, 3, 5]]
y2 = model.predict(x2)
s = model.score(X, Y)
print(y2,s)
