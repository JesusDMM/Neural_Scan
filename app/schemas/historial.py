from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

class TumorDetectado(BaseModel):
    type: str
    certeza: float
    evaluacion: Optional[str] = None

    class Config:
        orm_mode = True

class HistorialDeteccion(BaseModel):
    id_paciente_medico: int
    url_imagen: str
    comentario: Optional[str] = None
    url_imagen_original: str
    fecha: datetime
    tumores: List[TumorDetectado]

    class Config:
        orm_mode = True

class HistorialDeteccionCreate(BaseModel):
    id_paciente_medico: int
    url_imagen: str
    comentario: Optional[str] = None
    url_imagen_original: str
    fecha: datetime
