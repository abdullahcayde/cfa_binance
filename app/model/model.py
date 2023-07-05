import pandas as pd
import joblib

# Assets dataframe
df_assets = pd.DataFrame({'id_asset' : [1,2,3],
                         'name' : ['BTCUSDT', 'ETHBTC', 'ETHUSDT']})

# model load
with open(f'/app/app/model/arima2.pkl', 'rb') as pkl:
    model = joblib.load(pkl)
