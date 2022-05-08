from matplotlib import style, tight_layout
import pandas as pd
import numpy as np
import datetime as dt
import investpy
import seaborn as sb
import matplotlib.pyplot as plt
import matplotlib.dates as mdate
import mplfinance as mpf
# from mpl_finance import candlestick_ohlc

now = dt.datetime.now()
start = (now + dt.timedelta(days=-30)).strftime("%d/%m/%Y") 
end = dt.datetime.now().strftime("%d/%m/%Y")

def LoadStocksData(company_stock):
    load_data = investpy.get_stock_historical_data(stock= company_stock, country= "vietnam", from_date=start, to_date=end)
    load_data.drop("Currency", axis=1, inplace=True) # delete collumn Currency
    return load_data

def candle_graph(company_stock):
    data_load = LoadStocksData(company_stock)
    colors = mpf.make_marketcolors(up="#00ff00",
                                   down="#ff0000",
                                   wick="inherit",
                                   edge="inherit",
                                    volume="in"
                                    )
    mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors)
    mpf.plot(data_load, figratio=(20, 12), type='candle',
             title = 'Candlestick ' + company_stock
            , mav=20, tight_layout=True
            ,style=mpf_style
            ,volume = False
            ,returnfig = True
            )
    return plt

# def graph(company_stock):
#     data_load = LoadStocksData(company_stock)
#     data_load = data_load[['Open', 'High', 'Low', 'Close']]
#     data_load.reset_index(inplace=True)
#     data_load['Date'] = data_load['Date'].map(mdate.date2num)

#     ax=plt.subplot()
#     ax.grid(True)
#     ax.set_axisbelow(True)
    
#     ax.xaxis_date()
#     candlestick_ohlc(ax, data_load.values, width=0.5, colorup='green', colordown='red')
#     return plt
