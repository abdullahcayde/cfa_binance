from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from model.model import model, df_assets


app = FastAPI()


class ID(BaseModel):
    id: int

    
@app.get("/")
def home():
    return {"health_check": "OK"}
    
    
# Get all assets
@app.get("/api/assets")
def assets(id: Optional[int] = None):
    if id:
        if id not in list(df_assets.id_asset):
            return "Please enter the id nummer between 1-3"
    
        if id in list(df_assets.id_asset):
            df_id = df_assets.loc[df_assets.id_asset == id]
            ids = list(df_id.id_asset)
            names = list(df_id.name)
            return {"data" : [{ "ids": ids,
                              "names" : names}]}
    else:
        ids = list(df_assets.id_asset)
        names = list(df_assets.name)
        return {"data" : [{ "ids": ids,
                          "names" : names}]}


# Predict tomorrow price
@app.get("/api/predict")
def predict(periods : Optional[int] = None):
    if periods:
        yhat = model.predict(n_periods = periods)
        return { "data" : {"prediction" : list(yhat)}  }
    
    else:
        yhat = model.predict(n_periods=1)
        return { "data" : {"prediction" : list(yhat)}  }
