#things to do
# 1. make database for each new stock i want to make y
# 2. make a method to make any new combo of stocks y
# 3. learn csvfiles
# 4. create abiltiy to update csv file by where previous history changes
# 5. remove column
# 6. make loop find end of values 
# 7. create method for making new graph not in main
# n. create line maker for graph 
#import streamlit as st
from datetime import date

import yfinance as yf


from plotly import graph_objs as go 

import pandas as pd 
import mplfinance as mpf 

i = 0
stocks = ("AAPL", "NDAQ", "AMD", "TSLA", "FB", "INTC", "LOW", "HD")

#potencial stocks AAPL NDAQ AMD TSLA FB INTC LOW HD
aple = yf.download( tickers = "AAPL", period = "1y", interval = "1d" )
nasdaq = yf.download( tickers = "ndaq", period = "1y", interval = "1d" )

aple.to_csv('AAPL.csv')
nasdaq.to_csv('NDAQ.csv')
aple.to_csv('AAPLtoNDAQ.csv')

df = pd.read_csv('AAPLtoNDAQ.csv')
cf = pd.read_csv('AAPL.csv')
vf = pd.read_csv('NDAQ.csv')

#while(i < 255):
 #   j = cf.loc[i, 'Open']
  #  k = vf.loc[i, 'Open']
  #  l = j/k
  #  df.loc[i, 'Open'] = 5.0
  #  i+=1

while(i < 230):
    j = cf.loc[i, 'Open']
    k = vf.loc[i, 'Open']
    l = j/k
    df.loc[i, 'Open'] = l

    j = cf.loc[i, 'High']
    k = vf.loc[i, 'High']
    l = j/k
    df.loc[i, 'High'] = l

    j = cf.loc[i, 'Low']
    k = vf.loc[i, 'Low']
    l = j/k
    df.loc[i, 'Low'] = l

    j = cf.loc[i, 'Close']
    k = vf.loc[i, 'Close']
    l = j/k
    df.loc[i, 'Close'] = l

    j = cf.loc[i, 'Adj Close']
    k = vf.loc[i, 'Adj Close']
    l = j/k
    df.loc[i, 'Adj Close'] = l
    i += 1



df.to_csv('AAPLtoNDAQ.csv')

#mpf.plot(
#            df,
#           type='candle',
#            title='Apple, March - 2020',
#            ylabel='Price ($)'
#        )