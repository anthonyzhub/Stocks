#! /usr/bin/python3

import plotly.express as px

def plotlyExample(tickerSymbol):

    df = px.data.stocks()
    fig = px.line(df, x='date', y='{}'.format(tickerSymbol)) # <= https://plotly.com/python-api-reference/generated/plotly.express.line.html
    fig.show()

plotlyExample("AAPL")