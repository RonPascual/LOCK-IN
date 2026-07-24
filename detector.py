from dataclasses import dataclass

from ultralytics import YOLO


PHONE_CLASS_ID = 67


@dataclass
class DetectionResult:
    phone_detected: bool
    phone_boxes: list


def load_model(model_path="yolov8n.pt"):
    return YOLO(model_path)


def detect_phone(model, frame, confidence=0.5):
    results = model(frame, stream=True, verbose=False, conf=confidence, classes=[PHONE_CLASS_ID])
    phone_boxes = []

    for result in results:
        for box in result.boxes:
            class_id = int(box.cls.item()) if hasattr(box.cls, "item") else int(box.cls)
            if class_id == PHONE_CLASS_ID:
                phone_boxes.append(box)

    return DetectionResult(phone_detected=bool(phone_boxes), phone_boxes=phone_boxes)