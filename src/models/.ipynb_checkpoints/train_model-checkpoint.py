import numpy as np, pandas as pd, matplotlib.pyplot as plt
import sys
sys.path.append('/Users/macbook/Desktop/projects/Github_Repositories/cfa_binance/docs')
from config import path_arima
from statsmodels.tsa.arima.model import ARIMA
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# Read Daily Data and select Asset 1 
df01 = pd.read_csv(f'{path_arima}/All_2017_01_01_to_2023_05_31_daily.csv')
df = df01.loc[df01.id_asset == 1]
df.index = df['timestamp']

# Train test split
to_row = int(len(df)*0.9) #==> get 90% data for train , 10% data for test

train_df = df[0:to_row]['close']
test_df = df[to_row:]['close']

train_data = list(train_df)
test_data = list(test_df)


