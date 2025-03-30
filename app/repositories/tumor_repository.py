from sqlalchemy.orm import Session
from app.models.tumor import TumoresDetectados
from app.schemas.tumor import TumorDetectadoCreate

class TumorDetectadoRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create_tumor(self, tumor: TumorDetectadoCreate):
        db_tumor = TumoresDetectados(
            id_deteccion=tumor.id_deteccion,
            type=tumor.type,
            certeza=tumor.certeza,
            evaluacion=tumor.evaluacion
        )
        self.db.add(db_tumor)
        self.db.commit()
        self.db.refresh(db_tumor)
        return db_tumor
