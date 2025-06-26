# decrypt_and_open.py
from cryptography.fernet import Fernet
from authenticate import authenticate_face
import os
import subprocess

FOLDER_PATH = os.path.join(os.getcwd(), "myfiles")

def load_key():
    return open("secret.key", "rb").read()

def decrypt_folder(folder_path):
    print("[🔒] Authenticating with face...")
    if not authenticate_face():
        print("[⛔] Face not recognized. Access denied.")
        return

    print("[✅] Face recognized. Decrypting files...")

    key = load_key()
    fernet = Fernet(key)

    for filename in os.listdir(folder_path):
        if filename.endswith(".enc"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "rb") as f:
                encrypted_data = f.read()
            try:
                decrypted_data = fernet.decrypt(encrypted_data)
                output_file = file_path.replace(".enc", "_decrypted.txt")
                with open(output_file, "wb") as f:
                    f.write(decrypted_data)
                subprocess.Popen(["notepad.exe", output_file])
                print(f"[📂] Opened: {output_file}")
            except Exception as e:
                print(f"[!] Failed to decrypt {filename}: {e}")

if __name__ == "__main__":
    decrypt_folder(FOLDER_PATH)
