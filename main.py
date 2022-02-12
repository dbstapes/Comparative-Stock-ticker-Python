import streamlit as st
from datetime import date

import yfinance as yf

from ploty import graph_objs as go 

import pandas as pd 
import mplfinance as mpf 

START = "2015-01-01"

TODAY = date.today().strftime("%Y-%m-%d")

st.title("Comparative Stocks")