from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sklearn.datasets import load_iris


iris = load_iris()


app = FastAPI()
model = joblib.load("day13/iris_model.pkl")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

@app.post("/predict")
def predict(data: IrisInput):
    prediction = model.predict([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])
    return {"species": iris.target_names[prediction[0]]}
