import cv2
import face_recognition
import pickle
import os
import numpy as np

def register_face():
    cam = cv2.VideoCapture(0)
    print("[📸] Please position your face and press 's' to capture.")

    while True:
        ret, frame = cam.read()
        if not ret:
            print("[❌] Failed to capture image.")
            break

        cv2.imshow("Face Capture", frame)

        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # Convert to RGB
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # ✅ Print type and shape
            print("👉 Type:", type(rgb_frame))
            print("👉 Dtype:", rgb_frame.dtype)
            print("👉 Shape:", rgb_frame.shape)

            # Save frame for manual check
            cv2.imwrite("debug_capture.jpg", frame)

            # Encode face
            try:
                encodings = face_recognition.face_encodings(rgb_frame)

                if encodings:
                    encoding = encodings[0]
                    os.makedirs("face_data", exist_ok=True)
                    with open("face_data/authorized_user.pkl", "wb") as f:
                        pickle.dump(encoding, f)
                    print("[✅] Face registered successfully!")
                else:
                    print("[⚠️] No face detected. Try again.")
            except Exception as e:
                print("[🔥] Encoding failed:", e)

            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register_face()
