from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from domain.schemas.client import ClientCreate, ClientUpdate, ClientResponse
from useCases.client import createClient, deleteClient, getClient, getClientById, updateClient
from dependencies import get_session

router = APIRouter(
    prefix="/cients",
    tags=["Clients"])

@router.post("/", response_model=ClientResponse)
def create_client(client: ClientCreate, session: Session = Depends(get_session)):
    return createClient.createClientUseCase(session,client)

@router.get("/", response_model=list[ClientResponse])
def get_client(session: Session = Depends(get_session)):
    return getClient.getClientUseCase(session)

@router.get("/{clientId}", response_model=ClientResponse)
def get_client_by_id(clientId: str, session: Session = Depends(get_session)):
    client = getClientById.getClientUseCase(session, clientId)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client

@router.delete("/{clientId}")
def delete_client(clientId: str, session: Session = Depends(get_session)):
    if not deleteClient.deleteClientUseCase(session, clientId):
        raise HTTPException(status_code=404, detail="Client not found")
    return {"message": "Client deleted successfully"}

@router.patch("/{clientId}", response_model=ClientResponse)
def update_client(clientId: str, clientData: ClientUpdate, session: Session = Depends(get_session)):
    client = updateClient.updateClientUseCase(session, clientId, clientData)
    if not client:
        raise HTTPException(status_code=404, detail="Client not found")
    return client