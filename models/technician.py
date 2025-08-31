from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select

class TechnicianResponse(SQLModel):
    technicianId: int
    name: str
    time: float


class TechnicianBase(SQLModel):
    name: str = Field(index=True)
    time: int | None = Field(default=None, index=True)
     

class Technician(TechnicianBase, table =True):
    technicianId: int | None = Field(default=None, primary_key=True)


