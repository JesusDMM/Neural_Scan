from fastapi import FastAPI
from app.controllers.medicos_controller import router as medicos_router

app = FastAPI()

app.include_router(medicos_router)