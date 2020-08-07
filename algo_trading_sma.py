import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf
import pandas_datareader as web

plt.style.use('fivethirtyeight')
startdate = '2019-07-01'
#df = yf.download('UOB.SG')

# UOB
#df = yf.download('UOB.SG', start=startdate)

# Starhub
#df = yf.download('CC3.SI', start=startdate)

# Keppel DC AJBU.SI
#df = yf.download('AJBU.SI', start=startdate)

# suntec reits T82U.SI
df = yf.download('T82U.SI', start=startdate)

# SIA C6L.SI
#df = yf.download('C6L.SI', start=startdate)
stocks = ['T82U.SI']
#df = web.DataReader(stocks, data_source='yahoo', start=startdate)
print(df)

df.to_csv('UOBSG.csv')

plt.figure(figsize=(12.2, 4.5))
# plt.xticks(rotation=45)
plt.plot(df['Close'], label='Close')
plt.title('Close Price History')
plt.xlabel('Date')
plt.ylabel('Price SGD')
plt.show()

# Calculate 30 days simple moving average (SMA)
SMA30 = pd.DataFrame()
SMA30['Adj Close Price'] = df.Close.rolling(window=30).mean()
# Calculate 100 days simple moving average (SMA)
SMA100 = pd.DataFrame()
SMA100['Adj Close Price'] = df.Close.rolling(window=100).mean()

plt.figure(figsize=(12.2, 4.5))
# plt.xticks(rotation=45)
plt.plot(df['Close'], label='Close')
plt.plot(SMA30['Adj Close Price'], label='SMA30', color='red')
plt.plot(SMA100['Adj Close Price'], label='SMA100', color='blue')
plt.legend(loc='upper left')
plt.show()

#Create a new data
data = pd.DataFrame()
data['Close'] = df['Close']
data['SMA30'] = SMA30['Adj Close Price']
data['SMA100'] = SMA100['Adj Close Price']

print(data)

#function for buy sell
def buy_sell(data):
    sigPriceBuy = []
    sigPriceSell = []
    flag = -1

    for i in range(len(data)):
        if data['SMA30'][i] > data['SMA100'][i]:
            if flag != 1:
                sigPriceBuy.append(data['Close'][i])
                sigPriceSell.append(np.nan)
                flag = 1
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        elif data['SMA30'][i] < data['SMA100'][i]:
            if flag != 0:
                sigPriceSell.append(data['Close'][i])
                sigPriceBuy.append(np.nan)
                flag = 0
            else:
                sigPriceBuy.append(np.nan)
                sigPriceSell.append(np.nan)
        else:
            sigPriceBuy.append(np.nan)
            sigPriceSell.append(np.nan)

    return (sigPriceBuy, sigPriceSell)

    #Store buy sell data

buy_sell = buy_sell(data)
data['Buy_Signal_Price'] = buy_sell[0]
data['Sell_Signal_Price'] = buy_sell[1]

print(data)

plt.figure(figsize=(12.2, 4.5))
# plt.xticks(rotation=45)
plt.plot(data['Close'], label='Close', alpha=0.35)
plt.plot(data['SMA30'], label='SMA30', color='red', alpha=0.35)
plt.plot(data['SMA100'], label='SMA100', color='blue', alpha=0.35)
plt.scatter(data.index, data['Buy_Signal_Price'], label='Buy', marker='^', color='green')
plt.scatter(data.index, data['Sell_Signal_Price'], label='Sell', marker='v', color='red')
plt.legend(loc='upper left')
plt.show()