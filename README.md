# 🚗 AI Driver Drowsiness Detection System

A real-time Computer Vision and AI-powered Driver Sleep Detection System developed using Python, OpenCV, and Dlib. The system continuously monitors a driver's eye movements through a webcam and detects signs of fatigue based on eye closure duration. If the driver's eyes remain closed for more than 3 seconds, an alert message and alarm sound are triggered to help prevent accidents caused by drowsiness.

---

## 📌 Project Overview

Driver fatigue is one of the leading causes of road accidents worldwide. This project aims to improve road safety by monitoring a driver's alertness in real time using facial landmark detection and Eye Aspect Ratio (EAR) analysis.

The system uses a webcam to detect the driver's face, track eye landmarks, calculate eye openness, and identify prolonged eye closure associated with drowsiness.

---

## ✨ Features

* Real-time webcam monitoring
* Facial landmark detection using Dlib
* Eye Aspect Ratio (EAR) based drowsiness detection
* Detects prolonged eye closure
* Visual warning message on screen
* Audio alarm notification
* Lightweight and efficient implementation
* Easy to deploy and customize

---

## 🛠️ Technologies Used

| Technology | Purpose                    |
| ---------- | -------------------------- |
| Python     | Core Programming Language  |
| OpenCV     | Real-Time Video Processing |
| Dlib       | Facial Landmark Detection  |
| NumPy      | Numerical Computation      |
| SciPy      | Distance Calculations      |
| Playsound  | Audio Alert System         |

---

## 📂 Project Structure

AI-Driver-Drowsiness-Detection-System

├── main.py

├── requirements.txt

├── README.md

├── alarm.wav

└── shape_predictor_68_face_landmarks.dat

---

## ⚙️ Installation

### 1. Clone the Repository

git clone https:https://github.com/vijaydevverse/AI-Driver-Drowsiness-Detection-System

### 2. Navigate to Project Folder

cd AI-Driver-Drowsiness-Detection-System

### 3. Create Virtual Environment

python -m venv drowsy_env

### 4. Activate Virtual Environment

Windows:

drowsy_env\Scripts\activate

### 5. Install Required Packages

pip install -r requirements.txt

### 6. Download Facial Landmark Model

Download:

shape_predictor_68_face_landmarks.dat

From:

https://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2

Extract the downloaded file and place it inside the project folder.

### 7. Run the Application

python main.py

---

## 🚀 How It Works

1. Webcam captures live video frames.
2. Dlib detects the driver's face.
3. Facial landmarks around the eyes are extracted.
4. Eye Aspect Ratio (EAR) is calculated.
5. If eyes remain closed for more than 5 seconds:

   * DROWSINESS ALERT! message is displayed.
   * Alarm sound is triggered.
6. Monitoring continues until the application is closed.

---

## 🎯 Applications

* Driver Safety Systems
* Smart Vehicles
* Fleet Monitoring
* Transportation Safety
* Industrial Operator Monitoring
* Fatigue Detection Research

---

## 🔮 Future Enhancements

* Yawning Detection (MAR)
* Head Pose Estimation
* Mobile Application Integration
* Driver Monitoring Dashboard
* Night Vision Support
* Email/SMS Emergency Alerts
* Deep Learning-Based Fatigue Detection

---

## 👨‍💻 Author

**Vijay Krishnan P.M.**

---

## ⭐ If you found this project useful, consider giving it a star on GitHub.
