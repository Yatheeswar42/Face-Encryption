## 🔐 Overview

This project allows users to:
- Register their face using a webcam.
- Encrypt individual files or folders using AES symmetric encryption.
- Automatically decrypt files after successful face authentication.
- Secure file keys and facial data locally on the system.

---

## 🛠️ Installation

### 1. Python Environment

- Recommended Python version: **3.11**
- Create a virtual environment (optional but recommended):

```bash
python -m venv facecrypt-env
.\facecrypt-env\Scripts\activate  # For Windows
````

### 2. Install Required Packages

Use the provided requirements file:

```bash
pip install -r requirements.txt
```

If using prebuilt binaries for `dlib`:

```bash
pip install dlib-bin==19.24.6
```

---

## 🚀 Usage

### Step 1: Register Your Face

Run the script to capture and encode your face:

```bash
python register_face.py
```

* Press **`s`** to capture your face using the webcam.
* Facial encoding is saved as `authorized_user.pkl`.

---

### Step 2: Encrypt Files or a Folder

Set the path of the folder or file in `encrypt_file.py`:

```python
FOLDER_PATH = r"C:\FaceCrypt\myfiles"
```

Then run:

```bash
python encrypt_file.py
```

This will:

* Generate an AES key
* Encrypt each file in the specified folder
* Save the key in `filekey.key`

---

### Step 3: Decrypt with Face Authentication

To decrypt files, run:

```bash
python decrypt_and_open.py
```

This will:

* Activate webcam and authenticate the user
* If authenticated, decrypt the files using the key

---

## 🧠 Technologies Used

* **Python 3.11**
* **OpenCV** – Camera access and image processing
* **face\_recognition** – Face detection and encoding
* **dlib** – Core facial recognition engine
* **cryptography** – AES encryption using Fernet

---

## 🔐 Security Considerations

* Facial data is stored locally and securely (`face_data/`)
* AES encryption ensures file confidentiality
* Face authentication prevents unauthorized decryption

---
