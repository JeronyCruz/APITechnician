from sqlmodel import Session
from Connection import engine

def get_session():
    with Session(engine) as session:
        yield session