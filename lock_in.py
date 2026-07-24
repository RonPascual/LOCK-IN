import cv2
import time

from actions import open_webpage
from countdown import CountdownState
from detector import detect_phone, load_model
from ui import draw_countdown, draw_phone_box, draw_status
from webcam import open_webcam, read_frame, release_webcam


def main():
    model = load_model("yolov8n.pt")
    cap = open_webcam(0)
    state = CountdownState(required_detection_time=5, absence_reset_time=10)

    print("Starting Phone Recognition. Press 'q' to quit.")

    try:
        while True:
            ret, frame = read_frame(cap)
            if not ret:
                print("Failed to grab frame")
                break

            detection = detect_phone(model, frame)
            update = state.update(detection.phone_detected, time.time())

            for box in detection.phone_boxes:
                draw_phone_box(frame, box)

            if update.started:
                print("Phone detected. Opening Website in...")
                print(state.required_detection_time)

            if update.countdown_second is not None and not update.started:
                print(update.countdown_second)

            if update.opened_website:
                open_webpage()

            if update.reset:
                print("Phone lost. Countdown reset.")

            draw_countdown(frame, state.current_countdown())
            if state.phone_detected:
                draw_status(frame, "Phone detected")

            cv2.imshow("Phone Recognition System", frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    finally:
        release_webcam(cap)
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()