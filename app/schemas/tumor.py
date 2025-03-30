from pydantic import BaseModel
from typing import Optional

class TumorDetectadoCreate(BaseModel):
    id_deteccion: int
    type: str
    certeza: float
    evaluacion: Optional[str] = None
