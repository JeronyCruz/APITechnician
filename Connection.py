from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text
import urllib.parse

DB_NAME = "TechnicianDB"

# Properly encoded URLs
MASTER_URL = (
    "mssql+pymssql://ODISSEO\\SQLEXPRESS/master?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
)

DATABASE_URL = (
    "mssql+pymssql://ODISSEO\\SQLEXPRESS/TechnicianDB?"
    "driver=ODBC+Driver+17+for+SQL+Server&"
    "trusted_connection=yes"
)

# Alternative URL format (try this if above doesn't work):
# MASTER_URL = "mssql+pyodbc://@ODISSEO\\SQLEXPRESS/master?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
# DATABASE_URL = "mssql+pyodbc://@ODISSEO\\SQLEXPRESS/TechnicianDB?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"

def ensure_database():
    try:
        master_engine = create_engine(MASTER_URL, isolation_level="AUTOCOMMIT")
        
        with master_engine.connect() as conn:
            result = conn.execute(
                text(f"SELECT name FROM sys.databases WHERE name = '{DB_NAME}'")
            )
            if not result.fetchone():
                conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
                print(f"Database '{DB_NAME}' created")
            else:
                print(f"Database '{DB_NAME}' already exists")
    except Exception as e:
        print(f"Error ensuring database exists: {e}")
        raise

def create_db_and_tables():
    ensure_database()
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

# Create engine after URL fix
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SessionDep = Annotated[Session, Depends(get_session)]