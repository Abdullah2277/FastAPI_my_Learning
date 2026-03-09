# schemas.py
# Pydantic models = shape of data coming IN and going OUT
# These are separate from SQLAlchemy models!

from pydantic import BaseModel, Field
from typing import Optional

# What the client sends when CREATING a product
class ProductCreate(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
    category: Optional[str] = None

# What the client sends when UPDATING a product
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)
    category: Optional[str] = None

# What WE send back to the client
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: Optional[str] = None
    in_stock: bool

    # This tells Pydantic to read data from SQLAlchemy
    # objects (not just plain dicts)
    model_config = {"from_attributes": True}