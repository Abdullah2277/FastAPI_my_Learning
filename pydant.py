from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Optional

class Item(BaseModel):
    name: str
    price: float = Field(gt=0, description="Price must be greater than 0")
    description: Optional[str] = None   # optional field
    in_stock: bool = True               # field with default value

