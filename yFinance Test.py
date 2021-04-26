#! /usr/bin/python3

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

def printHistory(stock, symbol):

    historicalData = stock.history(period="1y") # <class 'pandas.core.frame.DataFrame'>

    historicalData["Close"].plot()
    plt.savefig("{} Graph.jpg".format(symbol))

def printDictionary(stock):
    
    for key in sorted(stock.keys()):
        print("{}: {}".format(key, stock[key]))

def plotlyExample(tickerSymbol):

    df = px.data.stocks()
    fig = px.line(df, x='date', y='{}'.format(tickerSymbol)) # <= https://plotly.com/python-api-reference/generated/plotly.express.line.html
    fig.show()

msft = yf.Ticker("MSFT")
# printDictionary(msft.info)
# printHistory(msft, "MSFT")
plotlyExample("AAPL")