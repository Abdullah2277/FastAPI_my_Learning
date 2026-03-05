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