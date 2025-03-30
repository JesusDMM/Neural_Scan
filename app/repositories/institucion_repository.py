from sqlalchemy.orm import Session
from app.models.instituciones import Institucion
from app.schemas.institucion import InstitucionCreate
from typing import List

class InstitucionRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_email(self, db: Session, email: str):
        return db.query(Institucion).filter(Institucion.correo == email).first()