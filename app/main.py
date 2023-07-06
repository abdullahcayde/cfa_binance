from typing import Optional
import pandas as pd
import sys
sys.path.append('/app/app/model')
from model import arima01, arima02, arima03, df_assets, df01, df02, df03
from fastapi import FastAPI

version = f"{sys.version_info.major}.{sys.version_info.minor}"

app = FastAPI()

@app.get("/")
async def home():
    message = f"Hello Abdullah Cay! From FastAPI running on Uvicorn with Gunicorn. Using Python {version}"
    return {"message": message}


@app.get("/api/assets")
async def assets():
        ids = list(df_assets.id_asset)
        names = list(df_assets.name)
        return {"data" : [{ "ids": ids,
                          "names" : names}]}


# Prediction tomorrow price by Asset id
@app.get("/api/predict/{assetid:int}")
async def predict_by_id(assetid, periods : Optional[int] = 1):
    if periods and (periods > 7 | periods <= 0) :
        return {"Error": "Periods can be between 1 and 7"}
    
    def get_prediction(df, arima):
        last_date = df['timestamp'].iloc[-1]
        last_date_price = df['close'].iloc[-1]
        asset_name = df_assets['name'].iloc[assetid - 1]
        yhat = arima.predict(n_periods=periods)
        tomorrow_price =  list(yhat)
        return {"data": {"prediction_tomorrow_price": tomorrow_price,
                "last_date": last_date,
                "last_date_price": last_date_price,
                "asset_name" : asset_name} }

    try:
        if assetid == 1:
            return get_prediction(df01, arima01)
        elif assetid == 2:
            return get_prediction(df02, arima02)
        elif assetid == 3:
            return get_prediction(df03, arima03)
        else:
            return {"Error": "Asset id must be between 1 and 3"}
    except Exception as e:
        return {"Error": str(e)}

    
# Predict all assests tomorrow price and desicion of "buy and sell"
@app.get("/api/predictall")
async def predict_by_id():
    def get_prediction(df, arima, assetid):
        last_date = df['timestamp'].iloc[-1]
        last_date_price = df['close'].iloc[-1]
        asset_name = df_assets['name'].iloc[assetid - 1]
        yhat = arima.predict(n_periods=1)
        tomorrow_price =  list(yhat)[0]
        price_difference = tomorrow_price - last_date_price
        price_difference_ratio = ( price_difference / tomorrow_price ) * 100
        
        if 10 < price_difference_ratio :
            buy_or_sell = "sell"
        elif -10 > price_difference:
            buy_or_sell = "buy"
        else:
            buy_or_sell = "neither buy nor sell"

        return {"prediction_tomorrow_price": tomorrow_price,
                "last_date": last_date,
                "last_date_price": last_date_price,
               "asset_name" : asset_name,
               "buy_or_sell" : buy_or_sell}     
    
    try:
        predictions = {
            "asset1": get_prediction(df01, arima01, 1),
            "asset2": get_prediction(df02, arima02, 2),
            "asset3": get_prediction(df03, arima03, 3)
        }
        return {"data": predictions}
    except Exception as e:
        return {"Error": str(e)}
    

# Prediction tomorrow price by Asset id and periods
@app.get("/api/predict/{assetid:int}")
async def predict_by_id(assetid):
    def get_prediction(df, arima):
        last_date = df['timestamp'].iloc[-1]
        last_date_price = df['close'].iloc[-1]
        asset_name = df_assets['name'].iloc[assetid - 1]
        yhat = arima.predict(n_periods=1)
        tomorrow_price =  list(yhat)[0]
        return {"data": {"prediction_tomorrow_price": tomorrow_price,
                "last_date": last_date,
                "last_date_price": last_date_price,
                "asset_name" : asset_name} }
