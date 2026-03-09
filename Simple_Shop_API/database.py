# database.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# This is the ONLY line you'd change for PostgreSQL/MySQL
# PostgreSQL would be: "postgresql://user:password@localhost/dbname"
# MySQL would be:      "mysql+pymysql://user:password@localhost/dbname"
DATABASE_URL = "sqlite:///./inventory.db"

# Engine = the actual connection to the database
# check_same_thread is SQLite-specific, always add it for SQLite
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}
)

# SessionLocal = a factory that creates database sessions
# Each request gets its own session (like a temporary workspace)
SessionLocal = sessionmaker(
    autocommit=False,  # we manually control when to save
    autoflush=False,
    bind=engine
)

# Base = parent class for all our database table models
class Base(DeclarativeBase):
    pass


# Dependency — gives each route its own DB session
# and closes it automatically when the request is done
def get_db():
    db = SessionLocal()  # open session
    try:
        yield db         # give it to the route
    finally:
        db.close()       # always close, even if error occurs