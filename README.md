# AI Driver Drowsiness Detection System

## Overview

This project is a Real-Time Driver Drowsiness Detection System developed using Python, OpenCV, and Dlib. The system monitors a driver's eyes through a webcam and detects drowsiness when the eyes remain closed for more than 5 seconds.

## Features

* Real-time webcam monitoring
* Eye closure detection
* Facial landmark detection using Dlib
* Audio alert using alarm.wav
* Visual warning message
* Computer Vision based safety system

## Technologies Used

* Python
* OpenCV
* Dlib
* NumPy
* SciPy
* Playsound

## Installation

1. Create a virtual environment

python -m venv drowsy_env

2. Activate the environment

drowsy_env\Scripts\activate

3. Install required packages

pip install -r requirements.txt

4. Download shape_predictor_68_face_landmarks.dat

5. Place the file in the project folder

6. Run the project

python main.py

## Project Files

* main.py
* requirements.txt
* alarm.wav
* README.md

## How It Works

The webcam continuously monitors the driver's eyes. If the eyes remain closed for more than 5 seconds, the system displays a "DROWSINESS ALERT!" message and plays an alarm sound.

## Author

Vijay Krishnan P.M.
