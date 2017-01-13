import pandas as pd

index_loc = ['a', 'b']
index_iloc = [1, 2]
data = [[1, 2, 3, 4], [5, 6, 7, 8]]

columns = ['one', 'two', 'three', 'four']
df1 = pd.DataFrame(data=data, index=index_loc, columns=columns)
df2 = pd.DataFrame(data=data, index=index_iloc, columns=columns)

# print(df1.loc['a'])
# print(df2.loc[1])
print(df1)
print(df2)
print(df1.loc[1])
print(df2.loc['a'])