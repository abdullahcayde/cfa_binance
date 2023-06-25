import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from pmdarima.arima import auto_arima
import joblib
import sys
sys.path.append('/Users/macbook/Desktop/projects/Github_Repositories/cfa_binance/docs')
from config import path_data_proceed, path_models 


# Read Daily Data and select Asset 1 
df = pd.read_csv(f'{path_data_proceed}/daily_proceed.csv')


# Train test split
to_row = int(len(df)*0.9) #==> get 90% data for train , 10% data for test

train_df = df[0:to_row]['close']
test_df = df[to_row:]['close']

train_data = list(train_df)
test_data = list(test_df)


# Fit ARIMA model
arima = auto_arima(train_data) 

# Serialize with joblib
joblib.dump(arima, f'{path_models}/arima.pkl')
