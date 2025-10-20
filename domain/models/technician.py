from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, Relationship
class Technician(SQLModel, table =True):
    __tablename__ = "technician"
    technicianId: int | None = Field(default=None, primary_key=True)
    name: str = Field(index=True, max_length=50)
    time: int | None = Field(default=None)
    technicianTypeId: Optional[int] = Field(default=None,foreign_key="tipoTecnico.technicianTypeId")
    
    tipo: Optional["TechnicianType"] = Relationship(back_populates="tecnicos")

