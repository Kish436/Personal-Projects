import yfinance as yf
import numpy as np  
import pandas as pd
from yfinance import data
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error as mse

ticker = 'GME'
data = yf.download(ticker, period='2y')

ClosePrices=data['Close'][ticker]
df = pd.DataFrame({'Close' : ClosePrices})

df['returns'] = np.log(df['Close'] / df['Close'].shift(1))

for lag in range(1,4):
    df['returns_lag' + str(lag)] = df['returns'].shift(lag)

df['Moving Average'] = df['returns'].rolling(5).mean()
df['Volatility'] = df['returns'].rolling(5).std()
df['Target'] = df['returns'].shift(-1)
df=df.dropna()

print(df.head())
print(df.shape)

trainingSplit = int(len(df) * 0.8)
train, test = df.iloc[:trainingSplit], df.iloc[trainingSplit:]

features = ['returns_lag1', 'returns_lag2', 'returns_lag3', 'Moving Average', 'Volatility']

Xtrain, ytrain = train[features], train['Target']
Xtest, ytest = test[features], test['Target']

model = LinearRegression()
model.fit(Xtrain, ytrain)
yPreds = model.predict(Xtest)

MSE = mse(ytest, yPreds)    
print(MSE)
print(len(train))
