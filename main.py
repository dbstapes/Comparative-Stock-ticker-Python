#things to do
# 1. make database for each new stock i want to make
# 2. make a method to make any new combo of stocks
# 3. learn csvfiles
# 4. create abiltiy to update csv file by where previous history changes
# n. create line maker for graph
import streamlit as st
from datetime import date

import yfinance as yf

from ploty import graph_objs as go 

import pandas as pd 
import mplfinance as mpf 

START = "2015-01-01"

TODAY = date.today().strftime("%Y-%m-%d")

st.title("Comparative Stocks")

stocks = ("AAPL", "NDAQ", "AMD", "TSLA", "FB", "INTC", "LOW", "HD")