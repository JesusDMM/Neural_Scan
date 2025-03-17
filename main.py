from fastapi import FastAPI
from app.controllers.medicos_controller import router as medicos_router
from app.controllers.pacientes_controller import router as pacientes_router

app = FastAPI()

app.include_router(medicos_router)
app.include_router(pacientes_router)