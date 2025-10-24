from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api import technicianRouter, technicianTypeRouter,clientRouter
from Connection import create_db_and_tables

app = FastAPI()
app.include_router(technicianRouter.router)
app.include_router(technicianTypeRouter.router)
app.include_router(clientRouter.router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")