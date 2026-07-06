from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "hello"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"hello {name}"}

class NumberInput(BaseModel):
    number: int

@app.post("/add")
def add(a: NumberInput, b: NumberInput):
    return {"result": a.number + b.number}
