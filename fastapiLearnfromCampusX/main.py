from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def greetings():
    return {"message": "Patient Management System API !"}

@app.get("/about")
def about():
    return {"message": "A completely functional API to manage your patient records !"}

# also learnt about docs and interactivity