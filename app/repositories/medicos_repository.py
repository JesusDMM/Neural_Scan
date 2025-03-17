from sqlalchemy.orm import Session
from app.models.medicos import Medico
from app.models.instituciones import Institucion

class MedicoRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_medico(self, cedula: str, id_institucion: int, correo: str, contraseña: str, nombres: str, apellidos: str, edad: int, especialidad: str):
        institucion = self.db.query(Institucion).filter(Institucion.id == id_institucion).first()
        if not institucion:
            raise ValueError(f"La institución con id {id_institucion} no existe.")
        
        medico = Medico(
            cedula=cedula,
            id_institucion=id_institucion,
            correo=correo,
            contraseña=contraseña,
            nombres=nombres,
            apellidos=apellidos,
            edad=edad,
            especialidad=especialidad
        )
        self.db.add(medico)
        self.db.commit()
        self.db.refresh(medico)
        return medico

    def get_medico(self, cedula: str):
        return self.db.query(Medico).filter(Medico.cedula == cedula).first()
    
    def get_medicos(self):
        return self.db.query(Medico).all()

    def update_medico(self, cedula: str, correo: str, contraseña: str, nombres: str, apellidos: str, edad: int, especialidad: str):
        medico = self.db.query(Medico).filter(Medico.cedula == cedula).first()
        if medico:
            medico.correo = correo
            medico.contraseña = contraseña
            medico.nombres = nombres
            medico.apellidos = apellidos
            medico.edad = edad
            medico.especialidad = especialidad
            self.db.commit()
            self.db.refresh(medico)
            return medico
        return None

    def delete_medico(self, cedula: str):
        medico = self.db.query(Medico).filter(Medico.cedula == cedula).first()
        if medico:
            self.db.delete(medico)
            self.db.commit()
            return True
        return False
