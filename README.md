
# 🤪 Useless Project — Emoji Login + Papadam Bump Counter

A delightfully useless web project that combines two unrelated concepts:
- **Emoji-based Facial Expression Login** 🎭
- **Papadam Bump Detection using OpenCV** 🍘

Perfectly weird and pointlessly fun!

---

## 🗂 Project Structure

```
useless-project/
│
├── app.py                       # Flask backend to serve login and upload logic
├── pappad.py                    # Image processing logic for bump detection
├── papadam.html                 # Bump counter upload interface (styled)
├── papadam.jpg                  # Sample papadam image
├── sindhi-masala-papad-1000x1000.jpg # Another sample image
├── README.md                    # This file ✨
│
├── static/
│   ├── contours.jpg             # Output with contour detection
│   ├── original.jpg             # Original uploaded image
│   ├── result.jpg               # Final image with bump contours
│   ├── threshold.jpg            # Thresholded image
│   ├── uploaded.jpg             # Raw uploaded file
│   └── models/                  # Face-api.js models
│       ├── face_expression_model-shard1
│       ├── face_expression_model-weights_manifest.json
│       ├── tiny_face_detector_model-shard1
│       └── tiny_face_detector_model-weights_manifest.json
│
└── templates/
    └── login.html              # Emoji-based facial expression login page
```

---

## 🚀 How to Run

### 1. 🧱 Install Requirements

```bash
pip install flask opencv-python matplotlib numpy
```

---

### 2. ▶️ Run the App

```bash
python app.py
```

Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## ✨ Features

### 🔐 Emoji Expression Login
- Facial expression converted to emoji
- Username generated via slider
- Pinky Promise drag-and-drop verification with confetti 🎉

### 🍘 Papadam Bump Counter
- Upload a papadam image
- Detects bumps via adaptive threshold + contouring
- Displays:
  - Original image
  - Thresholded version
  - Bump-detected image
  - Total bump count 💨

---

## 📁 Notes
- All facial recognition models (`face-api.js`) are loaded from `/static/models`.
- All images saved/processed are stored in `/static/`.

---

## 📸 Demo

![Login Page]<img width="1349" height="594" alt="login page (1)" src="https://github.com/user-attachments/assets/ceadc769-05c9-419a-afaa-d06bb18699cb" />
![Captcha Page]<img width="1353" height="589" alt="login page (2)" src="https://github.com/user-attachments/assets/fd28839a-257e-43a8-935a-2fd22e331614" />
![Papadam Counter]<img width="1365" height="598" alt="Screenshot 2025-08-02 035459" src="https://github.com/user-attachments/assets/5dc7c401-a4ee-4593-90e0-bb69968aef14" />

---

## 🧠 Why?
Why not.

---

## 🧽 License

Free to use. Just don’t sell papadams with this.
