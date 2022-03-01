#things to do
# 1. make database for each new stock i want to make y
# 2. make a method to make any new combo of stocks y
# 3. learn csvfiles y
# 4. create abiltiy to update csv file by where previous history changes
# 5. remove column y
# 6. take values from gui and place into graph
# 6. make loop find end of values y
# 7. create method for making new graph not in main 
# n. create line maker for graph 
#import streamlit as st
from datetime import date

import yfinance as yf


from plotly import graph_objs as go 

import pandas as pd 
import mplfinance as mpf 

def graph(numerator, denominator, length, size):
    i = 0
    stocks = ("AAPL", "NDAQ", "AMD", "TSLA", "FB", "INTC", "LOW", "HD")

    
    aple = yf.download( tickers = numerator, period = length, interval = size )
    nasdaq = yf.download( tickers = denominator, period = length, interval = size )

    aple.to_csv('AAPL.csv')
    nasdaq.to_csv('NDAQ.csv')
    aple.to_csv('AAPLtoNDAQ.csv')

    df = pd.read_csv('AAPLtoNDAQ.csv')
    cf = pd.read_csv('AAPL.csv')
    vf = pd.read_csv('NDAQ.csv')

    while(i < len(df)):
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



    df.Date = pd.to_datetime(df.Date)
    df = df.set_index('Date')
    df.to_csv('AAPLtoNDAQ.csv')
    mpf.plot(df, type = 'candle', style = 'charles' )
