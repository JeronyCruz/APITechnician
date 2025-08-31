from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine,Session
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

DB_NAME = "TechnicianDB"

MASTER_URL = (
    "mssql+pyodbc://ODISSEO\\SQLEXPRESS/master?"
    "driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

# Conexión final a tu BD real
DATABASE_URL = (
    f"mssql+pyodbc://ODISSEO\\SQLEXPRESS/{DB_NAME}?"
    "driver=ODBC+Driver+17+for+SQL+Server"
    "&trusted_connection=yes"
)

def ensure_database():
    master_engine = create_engine(MASTER_URL, isolation_level="AUTOCOMMIT")

    with master_engine.connect() as conn:
        result = conn.execute(
            text(f"SELECT name FROM sys.databases WHERE name = '{DB_NAME}'")
        )
        if not result.fetchone():
            conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
            print(f"Base de Datos '{DB_NAME}' creada")

        else:
            print(f"Base de datos '{DB_NAME}' ya existe")

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False,bind=engine)

def create_db_and_tables():
    ensure_database()
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]