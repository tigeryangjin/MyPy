from pandas import Series

obj = Series([4, 7, -5, 3])
obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas']
obj3 = Series(sdata)
