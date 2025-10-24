from sqlalchemy.orm import Session
from sqlmodel import select
from domain.models.client import Client

def create(db:Session, client: Client) -> Client:
    db.add(client)
    db.commit()
    db.refresh(client)
    return client

def getAll(db:Session) -> list[Client]:
    return db.exec(select(Client)).all()

def getById(db: Session, clientId: str) -> Client | None:
    return db.get(Client, clientId)

def delete(db: Session, clientId: str) -> bool:
    client = db.get(Client, clientId)
    if not client:
        return False
    db.delete(client)
    db.commit()
    return True

def update(db: Session, client: Client) -> Client:
    db.add(client)
    db.commit()
    db.refresh(client)
    return client