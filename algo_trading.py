import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

plt.style.use('fivethirtyeight')
#df = yf.download('UOB.SG')

# UOB
#df = yf.download('UOB.SG', start='2019-07-01')

# Starhub
#df = yf.download('CC3.SI', start='2019-07-01')

# Keppel DC AJBU.SI
df = yf.download('AJBU.SI', start='2019-07-01')

# suntec reits T82U.SI
df = yf.download('T82U.SI', start='2019-07-01')

# SIA C6L.SI
df = yf.download('C6L.SI', start='2019-07-01')

print(df)

df.to_csv('UOBSG.csv')

plt.figure(figsize=(12.2, 4.5))
#plt.xticks(rotation=45)
plt.plot(df['Close'], label='Close')
plt.title('Close Price History')
plt.xlabel('Date')
plt.ylabel('Price SGD')
plt.show()

# Calculate the MACF and signal line indicator
# Calculate short Term exponential moving average (EMA)
shortEMA = df.Close.ewm(span=12, adjust=False).mean()
# Calculate long Term exponential moving average (EMA)
longEMA = df.Close.ewm(span=26, adjust=False).mean()
# Calculate MACD line
MACD = shortEMA - longEMA
# Calculate signal line
signal = MACD.ewm(span=9, adjust=False).mean()


plt.figure(figsize=(12.2, 4.5))
#plt.xticks(rotation=45)
plt.plot(df.index, MACD, label='UOBSG MACD', color='red')
plt.plot(df.index, signal, label='Signal Line', color='blue')
plt.legend(loc='upper left')
plt.show()

df['MACD'] = MACD
df['Signal Line'] = signal


print (df)

def buy_sell(signal):
    Buy = []
    Sell = []
    flag = -1

    for i in range(0, len(signal)):
        if signal['MACD'][i] > signal['Signal Line'][i]:
            Sell.append(np.nan)
            if flag != 1:
                Buy.append(signal['Close'][i])
                flag = 1
            else:
                Buy.append(np.nan)
        elif signal['MACD'][i] < signal['Signal Line'][i]:
            Buy.append(np.nan)
            if flag != 0:
                Sell.append(signal['Close'][i])
                flag = 0
            else:
                Sell.append(np.nan)
        else:
            Buy.append(np.nan)
            Sell.append(np.nan)

    return (Buy, Sell)

# create buy sell colum
a = buy_sell(df)
df['Buy_Signal_Price'] = a[0]
df['Sell_Signal_Price'] = a[1]

print (df)

plt.figure(figsize=(12.2, 4.5))
plt.scatter(df.index, df['Buy_Signal_Price'], color='green', label='Buy', marker='^', alpha=1)
plt.scatter(df.index, df['Sell_Signal_Price'], color='red', label='Sell', marker='v', alpha=1)
plt.plot(df['Close'], label='Close', alpha=0.35)
#plt.plot(df['MACD'], label='UOBSG MACD', color='yellow', alpha=0.35)
#plt.plot(df['Signal Line'], label='Signal Line', color='grey', alpha=0.35)
plt.title('Close Price Buy & Sell Signal')
plt.xlabel('Date')
plt.ylabel('Price SGD')
plt.legend(loc='upper left')
plt.show()