from sqlalchemy import Column, Integer, String, Float, Enum, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
import enum

Base = declarative_base()

class EvaluacionEnum(str, enum.Enum):
    Correcto = "Correcto"
    Incorrecto = "Incorrecto"

class TumoresDetectados(Base):
    __tablename__ = 'tumores_detectados'

    id_tumor = Column(Integer, primary_key=True, index=True)
    id_deteccion = Column(Integer, nullable=False)
    type = Column(Enum('Glioma', 'Meningioma', 'Pituitary', name="tumor_types"), nullable=False)
    certeza = Column(Float, nullable=False)
    evaluacion = Column(Enum(EvaluacionEnum), default=None)
