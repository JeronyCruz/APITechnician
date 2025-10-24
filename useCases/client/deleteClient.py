from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client
from domain.schemas.client import ClientCreate
from infrastructure.repositories.clientRepository import (
    delete,
)

def deleteClientUseCase(session: Session, clientId: str) -> bool:
    return delete(session, clientId)