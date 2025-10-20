from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from api import technicianRouter, technicianTypeRouter

app = FastAPI()
app.include_router(technicianRouter.router)
app.include_router(technicianTypeRouter.router)



@app.get("/", include_in_schema=False)
def root():
    return RedirectResponse(url="/docs")