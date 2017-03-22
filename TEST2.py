import numpy as np
import pandas as pd

data1 = pd.DataFrame({'item': ['a', 'b', 'c', 'd'], 'in_qty': [1, 3, 5, 7]})
data2 = pd.DataFrame({'item': ['a', 'b', 'c', 'e'], 'out_qty': [2, 3, 6, 10]})

print(data1)
print(data2)
# print(pd.merge(data1,data2,how='inner'))
print(pd.merge(data1,data2))
print(data1.combine_first(data2))
