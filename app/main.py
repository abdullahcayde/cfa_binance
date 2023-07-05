from typing import Optional
import pandas as pd
import sys
sys.path.append('/app/app/model')
from model import model, df_assets

from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

df = pd.read_csv('/app/data/proceed/daily_proceed.csv')

@app.get("/")
async def read_root():
    message = f"Hello Abdullah Cay! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.get("/page01")
async def read_root():
        ids = list(df_assets.id_asset)
        names = list(df_assets.name)
        return {"data" : [{ "ids": ids,
                          "names" : names}]}
    
# Predict tomorrow price
@app.get("/predict")
def predict(periods : Optional[int] = None):
    last_date = df['timestamp'].iloc[-1]
    last_date_price = df['close'].iloc[-1]
    if periods:
        yhat = model.predict(n_periods = periods)
        return { "data" : {"prediction" : list(yhat)},
                 "last_date" :  last_date,
                  "last_date_price" :last_date_price}
    else:
        yhat = model.predict(n_periods=1)
        tomorrow_price =  list(yhat)[0]
        price_difference = tomorrow_price - last_date_price
        price_difference_ratio = ( price_difference / tomorrow_price ) * 100
        if 10 < price_difference_ratio :
            buy_or_sell = "sell"
        elif -10 > price_difference:
            buy_or_sell = "buy"
        else:
            buy_or_sell = "neither buy nor sell"

        
        return { "data" :{ "prediction_tomorrow_price" : tomorrow_price,
                                     "last_date" :  last_date,
                                     "last_date_price" :last_date_price},
                                     "price_difference-$" :  price_difference,
                                     "price_difference_ratio-%" : price_difference_ratio,
                                     "buy_or_sell" : buy_or_sell}
