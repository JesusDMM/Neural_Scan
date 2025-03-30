from fastapi import APIRouter, UploadFile, File, Depends, Form
from sqlalchemy.orm import Session
from app.sql.database import get_db
from app.models.historial import HistorialDetecciones
from app.models.tumor import TumoresDetectados
from app.repositories.historial_repository import HistorialDeteccionRepository
from app.repositories.tumor_repository import TumorDetectadoRepository
from app.schemas.historial import HistorialDeteccionCreate
from app.schemas.tumor import TumorDetectadoCreate
from app.utils.yolo_inference import YOLOInference
from datetime import datetime
import shutil
import os
import uuid

router = APIRouter()

yolo_model = YOLOInference("app/model/Model_Neural_Scan.onnx")

@router.post("/procesar_imagen")
def procesar_imagen(
    file: UploadFile = File(...),
    id_paciente_medico: int = Form(...),
    comentario: str = Form(None),
    db: Session = Depends(get_db)
):
    unique_id = str(uuid.uuid4())
    original_image_name = f"original_{unique_id}.jpg"
    original_image_path = os.path.join("app/public/images", original_image_name)

    # Crear la carpeta si no existe
    os.makedirs("app/public/images", exist_ok=True)

    with open(original_image_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    with open(original_image_path, "rb") as image_file:
        image_bytes = image_file.read()

    inference_results = yolo_model.predict(image_bytes)

    historial_data = HistorialDeteccionCreate(
        id_paciente_medico=id_paciente_medico,
        url_imagen_original=original_image_name,
        url_imagen=inference_results["inference_image"],
        comentario=comentario,
        fecha=datetime.utcnow()
    )
    repo_history = HistorialDeteccionRepository(db)
    repo_tumor = TumorDetectadoRepository(db)
    
    historial_entry = repo_history.create_historial(historial=historial_data)

    for tumor, certeza in zip(inference_results["predictions"], inference_results["confidences"]):
        tumor_data = TumorDetectadoCreate(
            id_deteccion=historial_entry.id_deteccion,
            type=tumor,
            certeza=certeza
        )
        repo_tumor.create_tumor(tumor=tumor_data)

    return {
        "id_deteccion": historial_entry.id_deteccion,
        "original_image": original_image_name,
        "inference_image": inference_results["inference_image"],
        "predictions": inference_results["predictions"],
        "confidences": inference_results["confidences"]
    }
