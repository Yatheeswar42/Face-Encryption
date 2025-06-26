import face_recognition
import cv2

image = face_recognition.load_image_file("obama.jpg")
print("👉 Shape:", image.shape, "| Dtype:", image.dtype)

try:
    encodings = face_recognition.face_encodings(image)
    if encodings:
        print("[✅] Encoding successful!")
    else:
        print("[⚠️] No face detected.")
except Exception as e:
    print("[🔥] Encoding failed:", e)
