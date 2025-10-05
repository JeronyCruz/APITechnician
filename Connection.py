from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, create_engine, Session
import os
from dotenv import load_dotenv

# ============================================================
# CONFIGURACIÓN DE CONEXIÓN
# ============================================================
load_dotenv()

# Obtener la URL de conexión desde el .env
DATABASE_URL = os.getenv("DATABASE_URL")

print("🧩 DATABASE_URL cargada:", DATABASE_URL) 

# ============================================================
# CREAR MOTOR DE CONEXIÓN
# ============================================================
engine = create_engine(DATABASE_URL, echo=True)

# ============================================================
# CREAR TABLAS EN LA BASE DE DATOS
# ============================================================
def create_db_and_tables():
    try:
        SQLModel.metadata.create_all(engine)
        print("✅ Tablas creadas correctamente en la base de datos PostgreSQL.")
    except Exception as e:
        print(f"❌ Error creando tablas: {e}")
        raise

# ============================================================
# SESIÓN DE CONEXIÓN PARA FASTAPI
# ============================================================
def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
