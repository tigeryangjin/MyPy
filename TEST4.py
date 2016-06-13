import numpy as np
import pandas as pd
from pandas import Series, DataFrame

pd.set_option('display.width', 200)

dates = pd.date_range('20150101', periods=5)
df = pd.DataFrame(np.random.randn(5, 4), index=dates, columns=list('ABCD'))
print(df)

stock_list = ['000001.XSHE', '000002.XSHE', '000568.XSHE', '000625.XSHE', '000768.XSHE', '600028.XSHG', '600030.XSHG', '601111.XSHG', '601390.XSHG', '601998.XSHG']
raw_data = DataAPI.MktEqudGet(secID=stock_list, beginDate='20150101', endDate='20150131', pandas='1')
df = raw_data[['secID', 'tradeDate', 'secShortName', 'openPrice', 'highestPrice', 'lowestPrice', 'closePrice', 'turnoverVol']]