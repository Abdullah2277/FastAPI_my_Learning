from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()

# A simple dependency — reusable logic
def get_query_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/products")
def list_products(params: dict = Depends(get_query_params)):
    return {"params": params}

