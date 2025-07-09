# visual_module.py
import cv2

def analyze_face_basic():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    emotion = "No face detected"
    if ret:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        emotion = "Face detected" if len(faces) > 0 else "No face detected"
    cap.release()
    return emotion
