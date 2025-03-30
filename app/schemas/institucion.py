from pydantic import BaseModel, EmailStr
from typing import Optional

class InstitucionBase(BaseModel):
    nombre: str
    correo: EmailStr

class InstitucionCreate(InstitucionBase):
    contraseña: str

class InstitucionResponse(InstitucionBase):
    id: int
    fecha_registro: Optional[str]
    
    class Config:
        from_attributes = True

class InstitucionLogin(BaseModel):
    correo: EmailStr
    contraseña: str