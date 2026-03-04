from fastapi import FastAPI,Depends,HTTPException

app = FastAPI()

# A simple dependency — reusable logic
def get_query_params(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.get("/products")
def list_products(params: dict = Depends(get_query_params)):
    return {"params": params}

# Real world use case — fake auth dependency
def verify_token(token: str):
    if token != "secret123":
        raise HTTPException(status_code=401, detail="Invalid token")
    return token

@app.get("/secure-data")
def secure_data(token: str = Depends(verify_token)):
    return {"data": "This is protected"}
