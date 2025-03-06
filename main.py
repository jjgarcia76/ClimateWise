from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

app = FastAPI()
model = joblib.load("climate_wise_model.pkl")

class ClimateInput(BaseModel):
    humidity: float
    pressure: float

@app.get("/")
def home():
    return {"message": "API Climate Wise está funcionando 🚀"}

@app.post("/predict/")
def predict(data: ClimateInput):
    features = np.array([[data.humidity, data.pressure]])
    prediction = model.predict(features)[0]
    return {"predicted_temperature": prediction}