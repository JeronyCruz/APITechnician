from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List

class TechnicianTypeBase(SQLModel):
    description: str = Field(index=True, max_length= 200)

class TechnicianType(TechnicianTypeBase, table = True):
    __tablename__ = "tipoTecnico"
    technicianTypeId: int | None = Field(default= None, primary_key= True)
    tecnicos: List["Technician"] = Relationship(back_populates="tipo")