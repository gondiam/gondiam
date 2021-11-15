# -*- coding: utf-8 -*-
"""
Created on Thu Jun 10 15:48:48 2021

@author: gdiaz
"""
#https://machinelearningmastery.com/time-series-prediction-lstm-recurrent-neural-networks-python-keras/
#OJO solo funciona con lookback = 1
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math
import keras
#!pip install yfinance
import yfinance as yf
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import mean_squared_error

#Data from yfinance of ETHEREUM
df = yf.download(tickers="ETC-EUR",period= '7d' ,interval='1m')
print(df)
Open = df['Open']
# normalize the dataset
scaler = MinMaxScaler(feature_range=(0, 1))
#Para que no de error
Open = Open.to_numpy()
Open = Open[:,np.newaxis]
Open= scaler.fit_transform(Open)
Open
dataset = Open
#train/test

train_size = int(len(dataset) * 0.9)
test_size = len(dataset) - train_size
train, test = dataset[0:train_size,:], dataset[train_size:len(dataset),:]
print(len(train), len(test))
#○Array of values into a dataset


# convert an array of values into a dataset matrix
def create_dataset(dataset, look_back=1):
	dataX, dataY = [], []
	for i in range(len(dataset)-look_back-1):
		a = dataset[i:(i+look_back), 0]
		dataX.append(a)
		dataY.append(dataset[i + look_back, 0])
	return np.array(dataX), np.array(dataY)



# reshape into X=t and Y=t+1
look_back = 1
trainX, trainY = create_dataset(train, look_back)
testX, testY = create_dataset(test, look_back)
print("train shape is: ",train.shape)
print("test shape is: ",test.shape)


# reshape input to be [samples, time steps, features]
trainX = np.reshape(trainX, (trainX.shape[0], 1, trainX.shape[1]))
testX = np.reshape(testX, (testX.shape[0], 1, testX.shape[1]))



# create and fit the LSTM network
model = Sequential()
model.add(LSTM(4, input_shape=(1, look_back)))
model.add(Dense(1))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(trainX, trainY, epochs=1, batch_size=1, verbose=1)
print (model.summary())


#Evaluation of the model
#model.evaluate(testX,testY)

# make predictions
trainPredict = model.predict(trainX)
testPredict = model.predict(testX)
# invert predictions
trainPredict = scaler.inverse_transform(trainPredict)
trainY = scaler.inverse_transform([trainY])
testPredict = scaler.inverse_transform(testPredict)
testY = scaler.inverse_transform([testY])
# calculate root mean squared error
trainScore = math.sqrt(mean_squared_error(trainY[0], trainPredict[:,0]))
print('Train Score: %.2f RMSE' % (trainScore))
testScore = math.sqrt(mean_squared_error(testY[0], testPredict[:,0]))
print('Test Score: %.2f RMSE' % (testScore))


#showing the original dataset in blue,
#the predictions for the training dataset in green,
#and the predictions on the unseen test dataset in red.
# shift train predictions for plotting
trainPredictPlot = np.empty_like(dataset)
trainPredictPlot[:, :] = np.nan
trainPredictPlot[look_back:len(trainPredict)+look_back, :] = trainPredict
# shift test predictions for plotting
testPredictPlot = np.empty_like(dataset)
testPredictPlot[:, :] = np.nan
testPredictPlot[len(trainPredict)+(look_back*2)+1:len(dataset)-1, :] = testPredict
# plot baseline and predictions
plt.title("Evolution of Ethereum of the last week")
plt.plot(scaler.inverse_transform(dataset),label="Original data")
plt.plot(trainPredictPlot,label="Prediction of the training data")
plt.plot(testPredictPlot,label="Prediction of the test data")
plt.legend()
plt.show()


