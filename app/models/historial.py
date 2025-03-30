from sqlalchemy import Column, Integer, String, Text, TIMESTAMP
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class HistorialDetecciones(Base):
    __tablename__ = 'historial_detecciones'

    id_deteccion = Column(Integer, primary_key=True, index=True)
    id_paciente_medico = Column(Integer, nullable=False)
    url_imagen = Column(String(255), unique=True, nullable=False)
    comentario = Column(Text, default=None)
    url_imagen_original = Column(String(255), unique=True, nullable=False)
    fecha = Column(TIMESTAMP, nullable=False)
