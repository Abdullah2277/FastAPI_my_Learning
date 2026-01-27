from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# LESSON 1 on get
# @app.get("/")
# def root():
#     return {"message": "Hello ! FastAPI is running !"}

# @app.get("/add")
# def add(num1: int, num2: int):
#     return {"sum": num1 + num2}

# @app.get("/subtract")
# def subtract(num1: int, num2: int):
#     return {"difference": num1 - num2}

# LESSON-2

class Numbers(BaseModel):
    num1: int
    num2: int

@app.post("/add")
def add(data: Numbers):
    result = data.num1 + data.num2
    return {"The Sum is ": result}