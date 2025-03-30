from ultralytics import YOLO

names = ['Glioma', 'Meningioma', 'Pituitary']

onnx_model = YOLO("../../model/Model_Neural_Scan.onnx")

imagen = "imagen_prueba.jpg"

results = onnx_model(imagen)

for result in results:
    for box in result.boxes:
        class_id = int(box.cls.item()) 
        confidence = float(box.conf.item())
        if confidence > 0.2: 
            print(f"Class: {names[class_id]}, Confidence: {confidence:.2f}")