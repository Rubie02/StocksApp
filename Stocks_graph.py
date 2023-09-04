
import datetime as dt
import investpy
import matplotlib.pyplot as plt
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
    mpf_style = mpf.make_mpf_style(base_mpf_style='nightclouds', marketcolors=colors) #black_background
    #mpf_style = mpf.make_mpf_style(marketcolors=colors) #light_background
    mpf.plot(data_load, figratio=(20, 12), type='candle',
             title = 'Candlestick ' + company_stock
            ,mav=20, tight_layout=True
            ,style=mpf_style
            ,volume = True
            ,returnfig = True
            )
    return plt
#candle_graph('VCB).show()
