from typing import Optional
import uuid
from sqlmodel import Field, SQLModel, Relationship
from fastapi import Depends, FastAPI, HTTPException, Query

class Client(SQLModel, table=True):
    __tablename__ = "client"
    clientId: uuid.UUID = Field(
        default_factory=uuid.uuid4, 
        primary_key=True,
        index=True,
        nullable=False
    )
    name: str = Field(index=True, max_length=100)
    email: str = Field(index=True, max_length=50)
    phone: Optional[str] = Field(default=None, max_length=15)