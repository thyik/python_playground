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

# Calculate Simple moving average (SMA)
SMA = df.Close.rolling(window=30).mean()
# Calculate Cumulative Moving Average (CMA)
CMA = df.Close.expanding(min_periods=30).mean()
# Calculate exponential moving average (EMA)
EMA = df.Close.ewm(span=26, adjust=False).mean()

plt.figure(figsize=(12.2, 4.5))
#plt.xticks(rotation=45)
plt.plot(df['Close'], label='Close', alpha=0.35)
plt.plot(df.index, SMA, label='SMA', color='red')
plt.plot(df.index, CMA, label='CMA', color='blue')
plt.plot(df.index, EMA, label='EMA', color='green')
plt.legend(loc='upper left')
plt.show()
