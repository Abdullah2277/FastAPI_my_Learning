from fastapi import FastAPI, Path, HTTPException
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

@app.get("/view")
def viewData():
    data = loadData()
    return data

@app.get("/viewPatient/{patientID}")
def viewPatient(patientID: str = Path(..., description = "ID of the Patient", example = "P001")):
    data = loadData()
    if patientID in data:
        return data[patientID]
    # return {"Error": "Patient Not Found !"}
    raise HTTPException(status_code = 404, detail = "Patient Not Found")