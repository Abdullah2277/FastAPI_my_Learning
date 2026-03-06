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

# 2. READ all products — GET /products
@app.get(
    "/products",
    response_model=list[ProductResponse]  # returns a LIST of products
)
def get_all_products():
    return list(inventory.values())  # return all products as a list


# 3. READ one product by ID — GET /products/{id}
@app.get(
    "/products/{product_id}",
    response_model=ProductResponse
)
def get_product(product_id: int):
    # If product doesn't exist, raise 404
    if product_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )
    return inventory[product_id]

# 4. FULL UPDATE — PUT /products/{id}
# Replaces the entire product with new data
@app.put(
    "/products/{product_id}",
    response_model=ProductResponse
)
def update_product(product_id: int, product: Product):
    if product_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )

    # Replace everything, but keep the same id
    updated_product = {
        "id": product_id,
        "name": product.name,
        "price": product.price,
        "stock": product.stock,
        "category": product.category
    }

    inventory[product_id] = updated_product
    return updated_product

# 5. PARTIAL UPDATE — PATCH /products/{id}
# Only updates the fields you send
@app.patch(
    "/products/{product_id}",
    response_model=ProductResponse
)
def partial_update_product(product_id: int, product: ProductUpdate):
    if product_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )

    existing = inventory[product_id]  # get current data

    # Only overwrite fields that were actually sent
    # If a field is None, it means client didn't send it — keep old value
    if product.name is not None:
        existing["name"] = product.name
    if product.price is not None:
        existing["price"] = product.price
    if product.stock is not None:
        existing["stock"] = product.stock
    if product.category is not None:
        existing["category"] = product.category

    return existing

# 6. DELETE a product — DELETE /products/{id}
@app.delete(
    "/products/{product_id}",
    status_code=status.HTTP_200_OK
)
def delete_product(product_id: int):
    if product_id not in inventory:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Product with id {product_id} not found"
        )

    deleted = inventory.pop(product_id)  # remove from dict
    return {"message": f"Product '{deleted['name']}' deleted successfully"}

# 7 Search by category — GET /products/search?category=electronics
@app.get(
    "/products/search/filter",
    response_model=list[ProductResponse]
)
def search_by_category(category: str):  # query parameter
    results = [
        p for p in inventory.values()
        if p["category"] and p["category"].lower() == category.lower()
    ]
    if not results:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"No products found in category '{category}'"
        )

    return results

    