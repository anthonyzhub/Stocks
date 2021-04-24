#! /usr/bin/python3

import yfinance as yf
import matplotlib.pyplot as plt

def printHistory(stock):

    historicalData = stock.history(period="1y") # <class 'pandas.core.frame.DataFrame'>
    print(historicalData)

    historicalData.plot(x="Close", y="Date")
    plt.show()

def printDictionary(stock):
    
    for key in sorted(stock.keys()):
        print("{}: {}".format(key, stock[key]))

msft = yf.Ticker("MSFT")
# printDictionary(msft.info)
printHistory(msft)