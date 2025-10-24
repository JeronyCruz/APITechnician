from pydantic import BaseModel, Field
from typing import Optional
import uuid

class ClientCreate(BaseModel):
    name: str = Field(..., max_length=100)
    email: str = Field(..., max_length=50)
    phone: Optional[str] = Field(default=None, max_length=15)

class ClientUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=100)
    email: Optional[str] = Field(None, max_length=50)
    phone: Optional[str] = Field(None, max_length=15)

class ClientResponse(BaseModel):
    clientId: uuid.UUID
    name: str
    email: str
    phone: Optional[str]

class config:
    from_attributes = True