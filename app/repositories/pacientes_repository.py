from sqlalchemy.orm import Session
from app.models.pacientes import Paciente
from app.models.paciente_medico import PacienteMedico
from app.models.medicos import Medico
from datetime import datetime

class PacienteRepository:
    def __init__(self, db: Session):
        self.db = db
        
    def create_paciente(self, curp: str, nombres: str, apellidos: str, genero: str, edad: int, lugar: str, cedula_medico: str):
        medico = self.db.query(Medico).filter(Medico.cedula == cedula_medico).first()
        if not medico:
            return None

        paciente = Paciente(
            curp=curp,
            nombres=nombres,
            apellidos=apellidos,
            genero=genero,
            edad=edad,
            lugar=lugar
        )

        self.db.add(paciente)
        self.db.flush()

        paciente_medico = PacienteMedico(
            cedula=cedula_medico,
            curp=curp,
            fecha=datetime.utcnow()
        )
        self.db.add(paciente_medico)

        self.db.commit()
        self.db.refresh(paciente)

        return paciente

    def get_paciente(self, curp: str):
        return self.db.query(Paciente).filter(Paciente.curp == curp).first()

    def get_all_pacientes(self):
        return self.db.query(Paciente).all()

    def update_paciente(self, curp: str, nombres: str, apellidos: str, genero: str, edad: int, lugar: str):
        paciente = self.get_paciente(curp)
        if not paciente:
            return None
        paciente.nombres = nombres
        paciente.apellidos = apellidos
        paciente.genero = genero
        paciente.edad = edad
        paciente.lugar = lugar
        self.db.commit()
        self.db.refresh(paciente)
        return paciente

    def delete_paciente(self, curp: str):
        paciente = self.get_paciente(curp)
        if not paciente:
            return None
        self.db.delete(paciente)
        self.db.commit()
        return paciente
