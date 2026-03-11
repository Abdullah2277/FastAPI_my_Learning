from fastapi import FastAPI
from pydantic import BaseModel
import json

app = FastAPI()

def loadData():
    with open("patients.json", "r") as f:
        data = json.load(f)
    return data

@app.get("/")
def greetings():
    return {"message": "Patient Management System API !"}

@app.get("/about")
def about():
    return {"message": "A completely functional API to manage your patient records !"}

