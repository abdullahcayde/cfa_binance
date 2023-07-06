import pandas as pd
import joblib

# Assets dataframe
df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})

# Dataframes with id number
df = pd.read_csv(f'/app/data/proceed/daily_proceed_all.csv')
df01 = df.loc[df.id_asset == 1]
df02 = df.loc[df.id_asset == 2]
df03 = df.loc[df.id_asset == 3]


# model01 load
with open(f'/app/app/model/arima01.pkl', 'rb') as pkl:
    arima01 = joblib.load(pkl)

# model02 load
with open(f'/app/app/model/arima02.pkl', 'rb') as pkl:
    arima02 = joblib.load(pkl)

# model03 load
with open(f'/app/app/model/arima03.pkl', 'rb') as pkl:
    arima03 = joblib.load(pkl)
