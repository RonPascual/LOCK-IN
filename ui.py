import cv2


def draw_phone_box(frame, box):
    x1, y1, x2, y2 = box.xyxy[0]
    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
    cv2.putText(frame, "Phone", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


def draw_countdown(frame, countdown_second):
    if countdown_second is None:
        return

    cv2.putText(frame, f"Opening website in {countdown_second}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)


def draw_status(frame, message):
    cv2.putText(frame, message, (20, 75), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)