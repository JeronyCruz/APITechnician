from typing import Optional

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, Relationship

class TechnicianBase(SQLModel):
    name: str = Field(index=True, max_length= 50)
    time: int | None = Field(default=None)
    technicianTypeId: Optional[int] = Field(default=None, foreign_key="tipoTecnico.technicianTypeId")
     

class Technician(TechnicianBase, table =True):
    __tablename__ = "technician"
    technicianId: int | None = Field(default=None, primary_key=True)
    
    tipo: Optional["TechnicianType"] = Relationship(back_populates="tecnicos")

class TechnicianResponse(SQLModel):
    # Este será el orden en el JSON
    technicianId: int
    name: str  
    time: Optional[float]
    technicianTypeId: Optional[int]
