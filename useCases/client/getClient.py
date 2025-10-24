from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client
from domain.schemas.client import ClientCreate
from infrastructure.repositories.clientRepository import (
    getAll,
)

def getClientUseCase(session: Session) -> list[Client]:
    return getAll(session)
