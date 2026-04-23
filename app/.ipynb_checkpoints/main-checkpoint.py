from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

# load trained model
model = joblib.load("model/model.pkl")

@app.get("/")
def home():
    return {"message": "Predictive Maintenance API is running"}

@app.post("/predict")
def predict(data: dict):

    try:
        features = np.array([
            data["temperature"],
            data["vibration"],
            data["pressure"]
        ]).reshape(1, -1)

        prediction = model.predict(features)[0]

        return {
            "prediction": int(prediction),
            "status": "Failure likely" if prediction == 1 else "Normal"
        }

    except Exception as e:
        return {"error": str(e)}