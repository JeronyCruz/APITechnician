from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class TechnicianType(SQLModel, table = True):
    __tablename__ = "tipoTecnico"
    technicianTypeId: int = Field(primary_key= True)
    description: str
    tecnicos: List["Technician"] = Relationship(back_populates="tipo")