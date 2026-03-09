# models.py
# SQLAlchemy models = actual database tables

from sqlalchemy import Column, Integer, String, Float, Boolean
from database import Base

class Product(Base):
    __tablename__ = "products"  # name of the table in the database

    # Each Column = one column in the table
    id       = Column(Integer, primary_key=True, index=True)
    name     = Column(String, nullable=False)       # NOT NULL
    price    = Column(Float, nullable=False)
    stock    = Column(Integer, default=0)
    category = Column(String, nullable=True)        # can be empty
    in_stock = Column(Boolean, default=True)