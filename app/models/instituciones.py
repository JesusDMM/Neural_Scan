from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.types import TIMESTAMP 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Institucion(Base):
    __tablename__ = 'instituciones'

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    fecha_registro = Column(TIMESTAMP, nullable=False)
