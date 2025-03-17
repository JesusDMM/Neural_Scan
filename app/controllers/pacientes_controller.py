from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.sql.database import get_db
from app.repositories.pacientes_repository import PacienteRepository
from app.utils.api_response import APIResponse
from app.schemas.paciente import PacienteCreate, PacienteUpdate

router = APIRouter()

@router.post("/pacientes")
def create_paciente(paciente: PacienteCreate, db: Session = Depends(get_db)):
    repo = PacienteRepository(db)
    paciente_creado = repo.create_paciente(
        paciente.curp, paciente.nombres, paciente.apellidos, paciente.genero, paciente.edad, paciente.lugar, paciente.cedula_medico
    )
    
    if paciente_creado == None:
        raise HTTPException(status_code=404, detail='Cedula de médico no encontrada.')

    return APIResponse.success(paciente_creado, "Paciente creado exitosamente")

@router.get("/pacientes/{curp}")
def get_paciente(curp: str, db: Session = Depends(get_db)):
    repo = PacienteRepository(db)
    paciente = repo.get_paciente(curp)
    if not paciente:
        return APIResponse.error("Paciente no encontrado", 404)
    return APIResponse.success(paciente, "Paciente encontrado")

@router.get("/pacientes")
def get_all_pacientes(db: Session = Depends(get_db)):
    repo = PacienteRepository(db)
    pacientes = repo.get_all_pacientes()
    return APIResponse.success(pacientes, "Pacientes encontrados")

@router.put("/pacientes/{curp}")
def update_paciente(curp: str, paciente: PacienteUpdate, db: Session = Depends(get_db)):
    repo = PacienteRepository(db)
    paciente_actualizado = repo.update_paciente(
        curp, paciente.nombres, paciente.apellidos, paciente.genero, paciente.edad, paciente.lugar
    )
    if not paciente_actualizado:
        return APIResponse.error("Paciente no encontrado", 404)
    return APIResponse.success(paciente_actualizado, "Paciente actualizado exitosamente")

@router.delete("/pacientes/{curp}")
def delete_paciente(curp: str, db: Session = Depends(get_db)):
    repo = PacienteRepository(db)
    paciente_eliminado = repo.delete_paciente(curp)
    if not paciente_eliminado:
        return APIResponse.error("Paciente no encontrado", 404)
    return APIResponse.success(paciente_eliminado, "Paciente eliminado exitosamente")
