from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

fake_db = {}

class Numbers(BaseModel):
    num1: int
    num2: int

