from pydantic import BaseModel
from enum import Enum

class GeneroEnum(str, Enum):
    masculino = "M"
    femenino = "F"

class PacienteCreate(BaseModel):
    curp: str
    nombres: str
    apellidos: str
    genero: GeneroEnum
    edad: int
    lugar: str
    cedula_medico: str

class PacienteUpdate(BaseModel):
    nombres: str
    apellidos: str
    genero: GeneroEnum
    edad: int
    lugar: str

    class Config:
        orm_mode = True
