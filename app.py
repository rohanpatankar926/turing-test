from fastapi import FastAPI
from pydantic import BaseModel
import joblib as jb
from fastapi.responses import JSONResponse
import numpy as np
import joblib
import uvicorn
app=FastAPI()

class InputData(BaseModel):
    features: list

@app.post("/predict")
def predict_model(features: InputData):
    print(features.features)
    
    input_featutes=np.array(features.features).reshape(1,-1)
    print(input_featutes)
    # print(type(input_featutes))
    model_load=joblib.load("models/model.pkl")
    print(model_load)
    prediction_res=model_load.predict(input_featutes)[0]
    return JSONResponse({"output_pred_res":prediction_res})

if __name__=="__main__":
    uvicorn.run(app=app,host="0.0.0.0",port=80)