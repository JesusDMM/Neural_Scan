from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class PacienteMedico(Base):
    __tablename__ = 'paciente_medico'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    cedula = Column(String(19), nullable=False)
    curp = Column(String(19), nullable=False)
    fecha = Column(TIMESTAMP, default=datetime.utcnow, nullable=False)
