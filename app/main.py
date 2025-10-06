from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Calculator API")

class Operation(BaseModel):
    a: float
    b: float

@app.get("/")
def root():
    return {"message": "Welcome to the Calculator API"}

@app.post("/add")
def add(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.a * op.b}

@app.post("/divide")
def divide(op: Operation):
    if op.b == 0:
        return {"error": "Division by zero is not allowed"}
    return {"result": op.a / op.b}
