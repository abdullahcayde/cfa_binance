import pandas as pd
import joblib

# arima model 
path = '/Users/macbook/Desktop/projects/Github_Repositories/cfa_binance/app/model'
with open(f'{path}/arima.pkl', 'rb') as pkl:
    model = joblib.load(pkl)


# Assets dataframe
df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})