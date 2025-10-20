from pydantic import BaseModel, Field
from typing import Optional

class TechnicianTypeCreate(BaseModel):
    description: str = Field(..., max_length=200)

class TechnicianTypeUpdate(BaseModel):
    description: Optional[str] = Field(None, max_length=200)

class TechnicianTypeResponse(BaseModel):
    technicianTypeId: int
    description: str

class Config:
        from_attributes = True