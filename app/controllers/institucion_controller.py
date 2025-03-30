from sqlalchemy.orm import Session
from app.sql.database import get_db
from app.repositories.institucion_repository import InstitucionRepository
from app.schemas.institucion import InstitucionCreate, InstitucionLogin
from fastapi import APIRouter, Depends, HTTPException
from app.utils.api_response import APIResponse

router = APIRouter()

@router.post("/login-institucion")
def login(login_data: InstitucionLogin, db: Session = Depends(get_db)):
    repo = InstitucionRepository(db)  
    institucion = repo.get_by_email(db, login_data.correo)
    
    if not institucion or institucion.contraseña != login_data.contraseña:
        return APIResponse.error("Credenciales incorrectas", 401)

    return APIResponse.success({"id": institucion.id}, "Login exitoso", 200)

