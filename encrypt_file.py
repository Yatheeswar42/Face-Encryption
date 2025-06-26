# encrypt_file.py
from cryptography.fernet import Fernet
import os

FOLDER_PATH = os.path.join(os.getcwd(), "myfiles")

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as f:
        f.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_folder(folder_path):
    if not os.path.exists("secret.key"):
        generate_key()
    key = load_key()
    fernet = Fernet(key)

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path) and not filename.endswith(".enc"):
            with open(file_path, "rb") as f:
                data = f.read()
            encrypted = fernet.encrypt(data)
            with open(file_path + ".enc", "wb") as f:
                f.write(encrypted)
            print(f"[+] Encrypted: {file_path}")

if __name__ == "__main__":
    encrypt_folder(FOLDER_PATH)
