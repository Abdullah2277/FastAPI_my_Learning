from fastapi import FastAPI, Path, HTTPException, Query
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

@app.get('/sort')
def sortPatients(sortBy: str = Query(..., description='Sort on the basis of bmi, height or weight'), order: str = Query('asc', description='sort in ascending or descending order')):
    sortingOptions = ['bmi', 'height', 'weight']
    orders = ['asc', 'desc']
    if sortBy not in sortingOptions:
        raise HTTPException(status_code=400, detail=f'Invalid Field. Select from {sortingOptions}')
    if order not in orders:
        raise HTTPException(status_code=400, detail=f'Invalid Field. Select from {orders}')