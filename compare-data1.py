from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd
yf.pdr_override()
from Investar import Analyzer


naverURL = ''
krx_list = pd.read_html('d:/My Project/stockAnalysis/PythonStockAnalysis/상장법인목록_220508.xls')

krx_list[0].종목코드 = krx_list[0].종목코드.map('{:06d}'.format)

#print(krx_list[0].종목코드)

mk = Analyzer.MarketDB()
df = mk.get_daily_price('005930', '2017-07-10', '2018-06.30')


plt.figure(figsize=(9, 6))
plt.suplot(2, 1, 1)
plt.title('Samsung Electronics (Investar Data')

plt.plot(df.index, df['close'], 'c', label='Close')
plt.legend(loc='best')
plt.subplot(2, 1, 2)
plt.bar(df.index, df['volume'], color='g', label='Volume')
plt.legend(loc='best')
plt.show()