from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy import text

DB_NAME = "TechnicianDB"

# URL para conectar a MySQL
MASTER_URL = "mysql+pymysql://root:IronMan01@localhost/mysql"
DATABASE_URL = f"mysql+pymysql://root:IronMan01@localhost/{DB_NAME}"

# Crear la base de datos si no existe
def ensure_database():
    try:
        master_engine = create_engine(MASTER_URL, isolation_level="AUTOCOMMIT")
        with master_engine.connect() as conn:
            result = conn.execute(text(f"SHOW DATABASES LIKE '{DB_NAME}'"))
            if not result.fetchone():
                conn.execute(text(f"CREATE DATABASE {DB_NAME}"))
                print(f"Database '{DB_NAME}' created")
            else:
                print(f"Database '{DB_NAME}' already exists")
    except Exception as e:
        print(f"Error ensuring database exists: {e}")
        raise

# Crear tablas
def create_db_and_tables():
    ensure_database()
    SQLModel.metadata.create_all(engine)

# Motor principal
engine = create_engine(DATABASE_URL, echo=True)

# Sesión tipo SQLModel (para usar .exec())
def get_session():
    with Session(engine) as session:
        yield session

# Para usar con FastAPI
SessionDep = Annotated[Session, Depends(get_session)]
