from fastapi import FastAPI, Request
from app.controllers.medicos_controller import router as medicos_router
from app.controllers.pacientes_controller import router as pacientes_router
from app.controllers.institucion_controller import router as instituciones_router
from app.controllers.login_controller import router as login_router
from app.controllers.detection_controller import router as detection_router


from fastapi.responses import JSONResponse
import logging


#from app.utils.yolo_inference import YOLOInference

app = FastAPI()

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logging.error(f"🚨 Error en {request.url}: {str(exc)}")
    return JSONResponse(
        status_code=500, 
        content={"message": str(exc)}
    )

#yolo_inference = YOLOInference(model_path="app/model/Model_Neural_Scan.onnx")

app.include_router(medicos_router)
app.include_router(pacientes_router)
app.include_router(instituciones_router)
app.include_router(login_router)
app.include_router(detection_router)