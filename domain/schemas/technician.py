from pydantic import BaseModel, Field
from typing import Optional

class TechnicianCreate(BaseModel):
    name: str = Field(..., max_length=50)
    time: int = None
    technicianTypeId: int = None

class TechnicianUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=50)
    time: Optional[int] = None
    technicianTypeId: Optional[int] = None

class TechnicianResponse(BaseModel):
    technicianId: int
    name: str  
    time: Optional[float]
    technicianTypeId: int

class Config:
        from_attributes = True