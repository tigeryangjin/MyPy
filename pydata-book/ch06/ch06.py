import pandas as pd
import sys
data=pd.read_csv('ex5.csv')
data.to_csv(sys.stdout,sep='|',na_rep='NULL')
