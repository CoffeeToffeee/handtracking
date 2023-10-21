import cv2
import mediapipe as mp
import time

# Setting up the camera
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils # allowing use to use prebuilt draw functions
# there aer some parameters here which you can change, im just using it do default

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # mediapipe uses rgb
    results = hands.process(imgRGB)
#   print(results.multi_hand_landmarks) checking coordinates

    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLMS)
            # drawing the dots on the hands

    cv2.imshow("Image", img)
    cv2.waitKey(1)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
