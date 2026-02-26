from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI()

fake_db = {}

class Numbers(BaseModel):
    num1: int
    num2: int

# CREATE
@app.post("/items/{item_id}")
def create_item(item_id: int, data: Numbers):
    fake_db[item_id] = data
    return {"message": "Created", "data": data}

# READ
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return fake_db.get(item_id, {"error": "Not found"})

# UPDATE (full replacement)
@app.put("/items/{item_id}")
def update_item(item_id: int, data: Numbers):
    fake_db[item_id] = data
    return {"message": "Updated", "data": data}

# PARTIAL UPDATE
@app.patch("/items/{item_id}")
def partial_update(item_id: int, data: Numbers):
    return {"message": "Partially updated"}

# DELETE
@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    fake_db.pop(item_id, None)
    return {"message": "Deleted"}