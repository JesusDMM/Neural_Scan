from sqlalchemy.orm import Session
from app.models.historial import HistorialDetecciones
from app.schemas.historial import HistorialDeteccionCreate

class HistorialDeteccionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_historial(self, historial: HistorialDeteccionCreate):
        db_historial = HistorialDetecciones(
            id_paciente_medico=historial.id_paciente_medico,
            url_imagen=historial.url_imagen,
            comentario=historial.comentario,
            url_imagen_original=historial.url_imagen_original,
            fecha=historial.fecha
        )
        self.db.add(db_historial)
        self.db.commit()
        self.db.refresh(db_historial)
        return db_historial
