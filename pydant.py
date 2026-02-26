from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    description: Optional[str] = None   # optional field
    in_stock: bool = True               # field with default value

@app.post("/products")
def create_product(item: Item):
    return item

# Response model — control what data is sent back
class ItemResponse(BaseModel):
    name: str
    price: float
    # notice: no description — we chose to hide it

