from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client
from domain.schemas.client import ClientCreate
from infrastructure.repositories.clientRepository import (
    create,
)

def createClientUseCase(session: Session, clientData: ClientCreate) -> Client:
    client = Client(**clientData.model_dump())
    return create(session, client)