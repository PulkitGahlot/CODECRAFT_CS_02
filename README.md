# 📱 Cryptographer: Text & Image Encryptor & Decryptor (Flutter + Python) 🔐🖼️

This is a mobile application built with **Flutter** and integrated with a **Python FastAPI backend** that allows users to:
- Encrypt and decrypt **text messages** using a Caesar Cipher (ASCII-based).
- Encrypt and decrypt **images** using XOR pixel manipulation.

Designed for **Cybersecurity Practice**, this tool demonstrates a simple yet powerful example of secure message and media exchange.

---

## 🚀 Features

### 📝 Text Encryption & Decryption
- Caesar Cipher with **custom shift key**.
- Input any ASCII-compatible message.
- Converts plain text to cipher text and vice versa.
- Buttons for **copy**, **paste**, and **share**.

### 🖼️ Image Encryption & Decryption
- Select image from gallery or camera.
- Apply XOR encryption/decryption using numeric key.
- Preview of selected image and processed image.
- Share or **download the encrypted/decrypted image**.
- Saves encrypted images to device **gallery**.

### 🛠️ Additional
- Fully mobile-friendly layout.
- App bar titles dynamically reflect user-selected operation.
- Clear separation between logic (backend) and UI (Flutter frontend).
- Compatible with Android 15 and MediaStore image saving.

---

## 🧠 How It Works

1. User lands on a Home Screen with **four options**:
   - Encrypt Text
   - Decrypt Text
   - Encrypt Image
   - Decrypt Image

2. Based on selection, user is navigated to:
   - `process_screen.dart` for text
   - `image_process_screen.dart` for images

3. The Flutter app sends a **POST request** to the local FastAPI backend:
   - For text: `/cipher` endpoint
   - For image: `/image_cipher` endpoint (uses XOR logic on RGB pixels)

4. The result is shown on the screen with options to **copy**, **share**, or **save**.

---

## 🧩 Project Structure

cryptographer/
├── lib/
│ ├── main.dart # Home screen (mode selection)
│ └── process_screen.dart # Encryption/Decryption screen
├── backend/
│ ├── requirements.txt # Python dependencies
│ ├── render.yaml # render configurations
│ └── main.py # FastAPI backend (Python)
├── android/ # Native Android config
├── pubspec.yaml # Dart dependencies
└── README.md # You're here!

---

## 🛠 Setup & Installation

1. Install Flutter: https://flutter.dev/docs/get-started/install
2. Clone the repository:
   ```sh
   git clone https://github.com/PulkitGahlot/CODECRAFT_CS_02.git
   cd CODECRAFT_CS_02
   ```
3. Install packages:
   ```sh
   flutter pub get
   ```
4. Connect your Android phone via USB or use an emulator.
5. Make sure your PC and phone are on the same Wi-Fi network
6. Install dependencies:
   ```sh
   pip install fastapi uvicorn pydantic pillow
   ```
7. Run the server:
   ```sh
   uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
   or use
   ```sh
   python -m uvicorn main:app --host 0.0.0.0 --port 8000 --reload
   ```
8. Replace 10.0.2.2 in Dart code with your PC's local IP (e.g. 192.168.x.x) so the app can reach the server.
9. Run the Application:
   ```sh
   flutter run
   ```

---

## 📦 Dependencies
  **Dart (Flutter)**
  - http
  - flutter/services (clipboard)
  - image_picker
  - path_provider
  - share_plus
  - google_fonts
  
  **Python**
  - fastapi
  - uvicorn
  - pydantic
  - pillow

---

## 📱 Screenshots

<img width="440" height="962" alt="Home_Screen" src="https://github.com/user-attachments/assets/b3378a4b-1b9c-4b84-9da4-011fe27e7ff3" />      <img width="441" height="970" alt="Text_Enryption_Screen" src="https://github.com/user-attachments/assets/7443f654-f274-42aa-bdf8-8d47f3c11048" />

<img width="436" height="964" alt="Image_Ecryption_Screen" src="https://github.com/user-attachments/assets/578a9f9b-7b52-4dc4-8b2c-e089ced5a834" />      <img width="440" height="972" alt="Image_Decryption_Screen" src="https://github.com/user-attachments/assets/ad382e2f-8dbf-4060-a963-5b17baec9a06" />

---

## 📦 Enhancements
- Added image_cipher API with XOR pixel encryption
- Integrated camera/gallery picker for images
- Used MediaStore-compliant saving with proper permissions
- UI refined with Spacer(), Column alignment, and text centering

---

## Download the application Here
- [Cryptographer](https://github.com/PulkitGahlot/CODECRAFT_CS_02/releases/download/v1.0.0/Cryptographer.apk)
- Or Scan the QR Code for Direct Download
  <img width="300" height="300" alt="app_download_qr" src="https://github.com/user-attachments/assets/2490b01f-e632-43f3-bc45-6bc0adabfb4f" />


## 👨‍💻 Author

Hi, I'm **Pulkit Gahlot**, a cyber security enthusiast and passionate to be an ethical hacker.

“A good hacker is the one who breaks systems, to build secure ones.”

Feel free to connect!
- **Linkedin**: [Pulkit Gahlot](https://linkedin.com/in/pulkit-gahlot)
- **X**: [Pulkit_Gahlot_](https://x.com/Pulkit_Gahlot_)
- **GitHub**: [PulkitGahlot](https://github.com/PulkitGahlot)
- **E-Mail**: [pulkitgahlot85@gmail.com](pulkitgahlot85@gmail.com)

Thank you for visiting my GitHub page!
