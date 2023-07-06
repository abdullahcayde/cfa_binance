import pandas as pd
from pmdarima.arima import auto_arima
import joblib
import sys
sys.path.append('/Users/macbook/Desktop/projects/Github_Repositories/cfa_binance/docs')
from config import path_data_proceed, path_models 


# Read Daily Data , Asset1, Asset2, Asset3
df = pd.read_csv(f'/app/data/proceed/daily_proceed_all.csv')
df01 = df.loc[df.id_asset == 1]
df02 = df.loc[df.id_asset == 2]
df03 = df.loc[df.id_asset == 3]

# Create Pkl 
def pkl_model(df, model_name):
    # Train Data
    train_df = df[0:]['close']
    train_data = list(train_df)

    # Fit ARIMA model
    arima = auto_arima(train_data)

    # Serialize with joblib
    joblib.dump(arima, f'{path_models}/{model_name}.pkl')

# Create all pkl models
pkl_model(df01, 'arima01')
pkl_model(df02, 'arima02')
pkl_model(df03, 'arima03')


