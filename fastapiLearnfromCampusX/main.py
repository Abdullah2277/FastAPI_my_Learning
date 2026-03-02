from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def greetings():
    return {"message": "Hello !"}

@app.get("/about")
def about():
    return {"message": "I am learning Fast API !"}

# also learnt about docs and interactivity