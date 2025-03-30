from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.repositories.institucion_repository import InstitucionRepository
from app.repositories.medicos_repository import MedicoRepository
from app.schemas.institucion import InstitucionLogin
from app.schemas.medicos import MedicoLogin
from app.utils.api_response import APIResponse
from app.sql.database import get_db

router = APIRouter()

@router.post("/login")
def login(login_data: InstitucionLogin, db: Session = Depends(get_db)):
    correo = login_data.correo
    contraseña = login_data.contraseña
    
    institucion_repo = InstitucionRepository(db)
    institucion = institucion_repo.get_by_email(db, correo)
    
    if institucion and institucion.contraseña == contraseña:
        return APIResponse.success({"id": institucion.id}, "Login exitoso", 200)
    
    medico_repo = MedicoRepository(db)
    medico = medico_repo.get_by_email(correo)
    
    if medico and medico.contraseña == contraseña:
        return APIResponse.success({"id": medico.cedula}, "Login exitoso", 200)
    
    return APIResponse.error("Credenciales incorrectas", 401)
