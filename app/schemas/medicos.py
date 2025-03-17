from pydantic import BaseModel

class MedicoCreate(BaseModel):
    cedula: str
    id_institucion: int
    correo: str
    contraseña: str
    nombres: str
    apellidos: str
    edad: int
    especialidad: str

class MedicoUpdate(BaseModel):
    correo: str
    contraseña: str
    nombres: str
    apellidos: str
    edad: int
    especialidad: str
