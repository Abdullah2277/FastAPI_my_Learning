from fastapi import FastAPI
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