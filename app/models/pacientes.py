from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Paciente(Base):
    __tablename__ = 'pacientes'

    curp = Column(String(19), primary_key=True, index=True)
    nombres = Column(String(255), nullable=False)
    apellidos = Column(String(255), nullable=False)
    genero = Column(String(10), nullable=False)
    edad = Column(Integer, nullable=False)
    lugar = Column(Text, nullable=False)
