from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client
from domain.schemas.client import ClientCreate
from infrastructure.repositories.clientRepository import (
    getById,
)

def getClientUseCase(session: Session, clientId: str) -> Client | None:
    return getById(session, clientId)
