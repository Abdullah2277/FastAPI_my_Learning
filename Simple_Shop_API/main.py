from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
from typing import Optional

app = FastAPI(title="Shop Inventory API")

# ─────────────────────────────────────────
# IN-MEMORY DATABASE (just a dictionary)
# In real projects this would be PostgreSQL,
# MongoDB etc. but dict is fine for learning
# ─────────────────────────────────────────
inventory = {}
next_id = 1  # auto-increment ID counter

# ─────────────────────────────────────────
# PYDANTIC MODELS
# ─────────────────────────────────────────

# Input model — what the CLIENT sends to US
class Product(BaseModel):
    name: str = Field(min_length=1, description="Product name")
    price: float = Field(gt=0, description="Price must be greater than 0")
    stock: int = Field(ge=0, description="Stock cannot be negative")
    category: Optional[str] = None  # optional field


# Update model — all fields optional (for PATCH)
class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    stock: Optional[int] = Field(default=None, ge=0)
    category: Optional[str] = None


# Response model — what WE send back to client
# Notice: we add "id" here which wasn't in input
class ProductResponse(BaseModel):
    id: int
    name: str
    price: float
    stock: int
    category: Optional[str] = None


# ─────────────────────────────────────────
# ROUTES
# ─────────────────────────────────────────

# 1. CREATE a product — POST /products
@app.post(
    "/products",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED  # 201 = resource was created
)
def create_product(product: Product):
    global next_id  # access the global counter

    new_product = {
        "id": next_id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "category": product.category
    }

    inventory[next_id] = new_product  # save to our dict
    next_id += 1  # increment for next product

    return new_product