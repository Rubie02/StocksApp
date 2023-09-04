import pandas as pd
import datetime as dt
import investpy

now = dt.datetime.now()
start = (now + dt.timedelta(days=-10)).strftime("%d/%m/%Y") 
end = now.strftime("%d/%m/%Y")

def inforCost(company):
    lst = []
    temp = investpy.get_stock_historical_data(stock= company,country="vietnam",from_date = start,to_date = end) 
    df = pd.DataFrame(temp)
    closeNow = df['Close'].iloc[-1]
    closePast = df['Close'].iloc[-2]
    change = closeNow-closePast
    changePercent = round((change*100)/closePast,1)
    vol = df['Volume'].iloc[-1]
    lst.append(closeNow)  
    lst.append(change)  
    lst.append(changePercent) 
    lst.append(vol)     
    return lst   
