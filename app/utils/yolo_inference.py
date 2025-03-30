from ultralytics import YOLO
from PIL import Image
import io
import os
import uuid

class YOLOInference:
    def __init__(self, model_path: str):
        self.model = YOLO(model_path)
        self.class_names = ['Glioma', 'Meningioma', 'Pituitary']
        self.output_dir = "app/public/images/"
        os.makedirs(self.output_dir, exist_ok=True)

    def predict(self, image_bytes: bytes):
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        results = self.model(image)

        unique_id = str(uuid.uuid4()) 
        inference_image_name = f"inference_{unique_id}.jpg"
        
        inference_image_path = os.path.join(self.output_dir, inference_image_name)

        for result in results:
            result.save(filename=inference_image_path)

        predictions = []
        confidences = []
        for result in results:
            for box in result.boxes:
                class_id = int(box.cls[0])
                confidence = float(box.conf[0])
                label = f"{self.class_names[class_id]}"
                predictions.append(label)
                confidences.append(confidence)

        return {
            'inference_image': inference_image_name,
            'predictions': predictions,
            'confidences': confidences
        }