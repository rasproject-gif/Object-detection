# detector.py
from ultralytics import YOLO
import cv2

class ObjectDetector:
    def __init__(self, model_path, target_class, conf_threshold=0.5):
        self.model = YOLO(model_path)
        self.target_class = target_class
        self.conf_threshold = conf_threshold
        self.class_names = self.model.names

    def detect_objects(self, frame):
        results = self.model(frame, verbose=False)
        detections = []

        for r in results:
            for box in r.boxes:
                cls_id = int(box.cls[0])
                label = self.class_names[cls_id]
                conf = float(box.conf[0])

                if label == self.target_class and conf >= self.conf_threshold:
                    x1, y1, x2, y2 = map(int, box.xyxy[0])
                    detections.append((x1, y1, x2, y2, label, conf))

        return detections
