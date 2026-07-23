import cv2
from ultralytics import YOLO

# Load the YOLOv8 model
model = YOLO('yolov8n.pt')  

# Initialize webcam capture
cap = cv2.VideoCapture(0)

PHONE_CLASS_ID = 67  # Class ID for 'cell phone' in COCO dataset

print("Starting Phone Recognition. Press 'q' to quit.")
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    # Perform inference on the frame
    results = model(frame, stream=True, verbose=False)  

    # Loop through every detected object aka box in the frame
    for result in results:
        # Look at each box and determine if it is a phone based on the class ID
        boxes = result.boxes
        for box in boxes:
            # if the detected object is a phone, draw a rectangle around it and label it
            if box.cls == PHONE_CLASS_ID:
                x1, y1, x2, y2 = box.xyxy[0]
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                cv2.putText(frame, 'Phone', (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    cv2.imshow('Phone Recognition System', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()