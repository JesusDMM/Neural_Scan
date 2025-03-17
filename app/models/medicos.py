from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Medico(Base):
    __tablename__ = 'medicos'

    cedula = Column(String(19), primary_key=True, index=True)
    id_institucion = Column(Integer, nullable=False)
    correo = Column(String(255), unique=True, nullable=False)
    contraseña = Column(String(255), nullable=False)
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    edad = Column(Integer)
    especialidad = Column(String(255), nullable=False)
