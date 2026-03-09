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

