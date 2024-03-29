import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import investpy
import datetime as dt

from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, Dropout, LSTM
import mplcursors
#pip install sklearn
#pip install tensorflow
#pip install scikit
#pip install keras

def Check(company):
    start = dt.datetime(2012, 1, 1).strftime("%d/%m/%Y")
    end = dt.datetime(2020, 1, 1).strftime("%d/%m/%Y")
    try:
        investpy.get_stock_historical_data(stock= company, country= 'vietnam', from_date = start, to_date = end) 
    except:
        return False
    return True

def Predict(company):
    #Load Data
    start = dt.datetime(2012, 1, 1).strftime("%d/%m/%Y")
    end = dt.datetime(2020, 1, 1).strftime("%d/%m/%Y")
    data = investpy.get_stock_historical_data(stock= company, country= 'vietnam', from_date = start, to_date = end) 

    #Prepare Data
    scaler=MinMaxScaler(feature_range=(0,1))
    scaled_data=scaler.fit_transform(data['Close'].values.reshape(-1,1))
    prediction_days = 60
    x_train=[]
    y_train=[]
    for x in range(prediction_days, len(scaled_data)):
        x_train.append(scaled_data[x-prediction_days:x, 0])
        y_train.append(scaled_data[x, 0])
    x_train, y_train = np.array(x_train), np.array(y_train)
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))

    #Build the Model
    model = Sequential()
    model.add(LSTM(units=50, return_sequences=True, input_shape=(x_train.shape[1], 1)))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50, return_sequences=True))
    model.add(Dropout(0.2))
    model.add(LSTM(units=50))
    model.add(Dropout(0.2))
    model.add(Dense(units=1)) #prediction of the next closing value
    model.compile(optimizer='adam', loss='mean_squared_error')
    model.fit(x_train, y_train, epochs=5, batch_size=32)

    '''Test the model accuracy on existing data'''

    #Load Test Data
    test_start=dt.datetime(2020, 1, 1).strftime("%d/%m/%Y")
    test_end=dt.datetime.now().strftime("%d/%m/%Y")
    test_data = data = investpy.get_stock_historical_data(stock= company, country= 'vietnam', from_date = test_start, to_date = test_end) 
    actual_prices=test_data['Close'].values
    total_dataset=pd.concat((data['Close'], test_data['Close']), axis=0)
    model_inputs = total_dataset[len(total_dataset)-len(test_data)-prediction_days:].values
    model_inputs = model_inputs.reshape(-1, 1)
    model_inputs = scaler.transform(model_inputs)

    # Make Predictions on Test Data
    x_test=[]
    for x in range(prediction_days, len(model_inputs)+1): #predict after 1 day
        x_test.append(model_inputs[x-prediction_days:x, 0])
    x_test=np.array(x_test)
    x_test=np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    predicted_prices=model.predict(x_test)
    predicted_prices=scaler.inverse_transform(predicted_prices)

    # Plot the test predictions
    plt.plot(actual_prices, color = "black", label=f"Actual {company} Price", visible = True)
    plt.plot(predicted_prices, color="red", label=f"Predicted {company} Price")
    plt.title(f"{company} Share Price")
    plt.xlabel("Time")
    plt.ylabel(f"{company} Share Price")
    plt.legend()
    plt.grid(color = 'green', linestyle = '--', linewidth = 0.5)
    mplcursors.cursor(hover=True)

    return predicted_prices[-1], plt
# a, b = Predict('VCB')
# b.show()

