# authenticate.py
import face_recognition
import cv2
import pickle

def authenticate_face():
    with open("face_data/authorized_user.pkl", "rb") as f:
        known_encoding = pickle.load(f)

    cam = cv2.VideoCapture(0)
    print("[INFO] Authenticating...")

    authenticated = False
    for _ in range(10):
        ret, frame = cam.read()
        if not ret:
            continue
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(rgb)
        for face_encoding in encodings:
            match = face_recognition.compare_faces([known_encoding], face_encoding)[0]
            if match:
                authenticated = True
                break
        if authenticated:
            break

    cam.release()
    return authenticated
