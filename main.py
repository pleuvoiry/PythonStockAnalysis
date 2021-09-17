from blockchain import exchangerates
from pandas_datareader import data as pdr
import yfinance as yf
import matplotlib.pyplot as plt

yf.pdr_override()


msft = pdr.get_data_yahoo('MSFT', start='2018-05-04')#, end='2019-09-07')
msft_dpc = (msft['Close'] - msft['Close'].shift(1)) / msft['Close'].shift(1) * 100
msft_dpc.iloc[0] = 0
msft_dpc_cs = msft_dpc.cumsum()
#print(msft.head())

#print(tmp_msft.tail())

#daily percent change
# *today change rate = { (today close price) - (yesterday close price) / (yesterday close price) } * 100

#Cumulative Sum
#  sec_dpc_cs is for cumsum of daily percentage change values

#Maximum Drawdown 최대 손실 낙폭
# lowest point - maximum point / lowest point

sec = pdr.get_data_yahoo('005930.KS', start='2018-05-04')#, end='2019-09-07')
sec_dpc = (sec['Close'] - sec['Close'].shift(1)) / sec['Close'].shift(1) * 100
sec_dpc.iloc[0] = 0
sec_dpc_cs = sec_dpc.cumsum()

plt.plot(sec.index, sec_dpc_cs, 'b', label='Samsung Electronics')
plt.plot(msft.index, msft_dpc_cs, 'r--', label='Microsoft')
plt.ylabel('Change %')
plt.grid(True)
plt.legend(loc='best')

plt.show()