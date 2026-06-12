import cv2
import dlib
import time
import threading

from scipy.spatial import distance
from playsound import playsound


# Alarm Sound
def alarm():
    playsound("alarm.wav")


# Eye Aspect Ratio
def eye_aspect_ratio(eye):

    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])

    ear = (A + B) / (2.0 * C)

    return ear


# Face Detector
detector = dlib.get_frontal_face_detector()

# Landmark Model
predictor = dlib.shape_predictor(
    "shape_predictor_68_face_landmarks.dat"
)

# Left Eye Points
LEFT_EYE = [36, 37, 38, 39, 40, 41]

# Right Eye Points
RIGHT_EYE = [42, 43, 44, 45, 46, 47]

EAR_THRESHOLD = 0.25

DROWSY_TIME = 3

closed_start_time = None

alarm_on = False

# Start Webcam
cap = cv2.VideoCapture(0)

print("Driver Drowsiness Detection Started")

while True:

    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )

    faces = detector(gray)

    for face in faces:

        landmarks = predictor(
            gray,
            face
        )

        left_eye = []
        right_eye = []

        for n in LEFT_EYE:
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            left_eye.append((x, y))

        for n in RIGHT_EYE:
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            right_eye.append((x, y))

        leftEAR = eye_aspect_ratio(left_eye)

        rightEAR = eye_aspect_ratio(right_eye)

        ear = (leftEAR + rightEAR) / 2

        for point in left_eye + right_eye:

            cv2.circle(
                frame,
                point,
                2,
                (0, 255, 0),
                -1
            )

        if ear < EAR_THRESHOLD:

            if closed_start_time is None:
                closed_start_time = time.time()

            elapsed = (
                time.time()
                - closed_start_time
            )

            cv2.putText(
                frame,
                f"Eyes Closed: {elapsed:.1f}s",
                (20, 50),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

            if elapsed >= DROWSY_TIME:

                cv2.putText(
                    frame,
                    "DROWSINESS ALERT!",
                    (50, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0, 0, 255),
                    3
                )

                if not alarm_on:

                    alarm_on = True

                    threading.Thread(
                        target=alarm,
                        daemon=True
                    ).start()

        else:

            closed_start_time = None

            alarm_on = False

    cv2.imshow(
        "Driver Drowsiness Detection",
        frame
    )

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()