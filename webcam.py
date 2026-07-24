import cv2


def open_webcam(index=0):
    cap = cv2.VideoCapture(index)
    if not cap.isOpened():
        raise RuntimeError("Error: Could not open webcam")
    return cap


def read_frame(cap):
    return cap.read()


def release_webcam(cap):
    cap.release()