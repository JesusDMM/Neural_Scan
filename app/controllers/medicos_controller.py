from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.medicos_repository import MedicoRepository
from app.schemas.medicos import MedicoCreate, MedicoUpdate
from app.sql.database import get_db
from app.utils.api_response import APIResponse

router = APIRouter()

@router.post("/medicos/")
def create_medico(medico: MedicoCreate, db: Session = Depends(get_db)):
    try:
        repo = MedicoRepository(db)
        nuevo_medico = repo.create_medico(
            medico.cedula, 
            medico.id_institucion, 
            medico.correo, 
            medico.contraseña, 
            medico.nombres, 
            medico.apellidos, 
            medico.edad, 
            medico.especialidad
        )
        return APIResponse.success(nuevo_medico, "Médico creado exitosamente", 201)
    except ValueError as e:
        return APIResponse.error(str(e), 400)

@router.get("/medicos/{cedula}")
def get_medico(cedula: str, db: Session = Depends(get_db)):
    repo = MedicoRepository(db)
    medico = repo.get_medico(cedula)
    
    if not medico:
        raise HTTPException(status_code=404, detail=APIResponse.error("Médico no encontrado", 404))
    
    return APIResponse.success(medico, "Médico encontrado", 200)

@router.get("/medicos")
def get_medicos(db: Session = Depends(get_db)):
    repo = MedicoRepository(db)
    medico = repo.get_medicos()
    
    if not medico:
        raise HTTPException(status_code=404, detail=APIResponse.error("Médicos no encontrados", 404))
    
    return APIResponse.success(medico, "Médicos encontrados", 200)

@router.put("/medicos/{cedula}")
def update_medico(cedula: str, medico: MedicoUpdate, db: Session = Depends(get_db)):
    repo = MedicoRepository(db)
    updated_medico = repo.update_medico(cedula, medico.correo, medico.contraseña, medico.nombres, medico.apellidos, medico.edad, medico.especialidad)
    if not updated_medico:
        raise HTTPException(status_code=404, detail=APIResponse.error("Error al actualizar un medico", 404))
    return APIResponse.success(updated_medico, "Médico actualizado correctamente", 200)

@router.delete("/medicos/{cedula}")
def delete_medico(cedula: str, db: Session = Depends(get_db)):
    repo = MedicoRepository(db)
    success = repo.delete_medico(cedula)
    if not success:
        raise HTTPException(status_code=404, detail="Médico no encontrado.")
    return APIResponse.success(None, "Médico eliminado correctamente", 200)
