import cv2
import mediapipe as mp
import time
import keyboard as kb

# Setting up the camera
cap = cv2.VideoCapture(1)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils  # allowing use to use prebuilt draw functions
pTime = 0
cTime = 0

while True:
    success, img = cap.read()
    # Mirror the image horizontally
    img = cv2.flip(img, 1)  # mediapipe uses rgb cameras usually give BGR
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    # drawing the dots and lines on the hands
    if results.multi_hand_landmarks:
        for handLMS in results.multi_hand_landmarks:
            for id, lm in enumerate(handLMS.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)

            mpDraw.draw_landmarks(img, handLMS, mpHands.HAND_CONNECTIONS)

    # Code to display FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)
