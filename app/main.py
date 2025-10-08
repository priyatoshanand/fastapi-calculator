from fastapi import FastAPI
from functions_framework import create_app
from pydantic import BaseModel

app = FastAPI()

class Operation(BaseModel):
    a: float
    b: float

@app.post("/add")
def add(op: Operation):
    return {"result": op.a + op.b}

@app.post("/subtract")
def subtract(op: Operation):
    return {"result": op.a - op.b}

@app.post("/multiply")
def multiply(op: Operation):
    return {"result": op.a * op.b}

# Cloud Functions entrypoint
def fastapi_entrypoint(request):
    return create_app(app)(request)
