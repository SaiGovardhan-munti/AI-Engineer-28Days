from pydantic import BaseModel
from fastapi import FastAPI
import joblib
import numpy

app = FastAPI()

vetorizer = joblib.load("vetorizer.pkl")
model = joblib.load("model.pkl")

class TextRequest(BaseModel):
    text: str


@app.post("/predict")
def predict(request: TextRequest):
    x = vetorizer.transform([request.text])
    prediction = model.predict(x)
    return {"label": prediction[0]}

@app.post("/explain")
def explian(request: TextRequest):
    x = vetorizer.transform([request.text])
    feature_names = vetorizer.get_feature_names_out()
    coefficients = model.coef_[0]
    top_indices =  numpy.argsort(numpy.abs(coefficients))[-5:]
    return {"words": [{"word": feature_names[i], "weight": coefficients[i]} for i in top_indices]}

