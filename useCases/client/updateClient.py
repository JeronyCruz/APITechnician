from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client
from domain.schemas.client import ClientUpdate
from infrastructure.repositories.clientRepository import (
    update,
    getById
)

def updateClientUseCase(session: Session, clientId: str, clientData: ClientUpdate) -> Client | None:
    client = getById(session, clientId)
    if not client:
        return None
    for key, value in clientData.model_dump(exclude_unset=True).items():
        setattr(client, key, value)
    return update(session, client)