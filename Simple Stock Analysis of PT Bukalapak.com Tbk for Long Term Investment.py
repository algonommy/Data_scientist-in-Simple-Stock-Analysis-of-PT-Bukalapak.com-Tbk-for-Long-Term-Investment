# -*- coding: utf-8 -*-
# Simple Stock Analysis of PT Bukalapak.com Tbk for Long Term Investment.ipynb


### Data Collection

import pandas_datareader.data as web

buka = web.DataReader('BUKA.JK', 'yahoo', start='2021-08-06', end='2021-11-13')
buka

buka = buka[['Adj Close']]. rename(columns={'Adj Close': 'Price'}).copy()
buka.tail(10)

"""Untuk lebih memahami data, mari kita plot menggunakan Matplotlib. Perpustakaan menyediakan banyak toolkit visualisasi."""

import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use('seaborn')

plt.figure(figsize=(16,10))
plt.plot(buka['Price'], '-')
plt.gcf().autofmt_xdate()
plt.title('BUKA Prices Since 2021', fontsize=20)
plt.xlabel('Date', fontsize=16)
plt.ylabel('Price in Rp', fontsize=16)
plt.show()

## Plot
def plot_time_series(data, title, x_label, y_label):
    plt.figure(figsize=(16,10))
    plt.plot(data, '-')
    plt.gcf().autofmt_xdate()
    plt.title(title, fontsize=20)
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    plt.show()

import numpy as np

price_IPO = buka['Price'][0]
price_2021 = buka['Price'][-1]
roi = np.log(price_2021 / price_IPO) * 100 # Logarithmic Return
print(f'Price on {buka.index[0].strftime("%d-%m-%y")}: Rp{round(price_IPO, 2)}')
print(f'Price on {buka.index[-1].strftime("%d-%m-%y")}: Rp{round(price_2021, 2)}')
print(f'Return of Investment: {round(roi, 2)}%')

## Data Analysis

buka['Price d+1'] = buka['Price'].shift(-1)
buka['ROI'] = np.log(buka['Price d+1'] / buka['Price']) * 100
buka

#Visualisasi ROI of BUKA Stock everyday
plot_time_series(buka['ROI'], 'ROI of BUKA Stock everyday', 'Date', 'ROI in %')

## Resampling
buka = buka[['ROI']].resample('1M').sum()
buka

#Visualisasi ROI of BUKA Stock every month
plot_time_series(buka['ROI'], 'ROI of BUKA Stock every month', 'Date', 'ROI in %')

buka.describe() #Operation Describe

def plot_time_series_with_summary(data, title, x_label, y_label):
    plt.figure(figsize=(16, 10))
    plt.plot(data, '-')
    plt.gcf().autofmt_xdate()
    plt.axhline(y=data.mean(), label='Mean', color='r')
    plt.fill_between(data.index, (data.mean()-data.std()), (data.mean()+data.std()), color='b', alpha=.1, label='Volatility')
    plt.title(title, fontsize=20)
    plt.xlabel(x_label, fontsize=16)
    plt.ylabel(y_label, fontsize=16)
    plt.legend()
    plt.show()

#Visualization Volatility ROI of BUKA Stock every month 
plot_time_series_with_summary(buka['ROI'], 'ROI of BUKA Stock every month', 'Date', 'ROI in %')

## Using Q-Q Plot
import statsmodels.api as sm
sm.qqplot(buka, line = '45').show()
