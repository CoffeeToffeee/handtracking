import HandTrackingModule as htm
import mediapipe as mp
import cv2
import pyautogui as pg
import time as t


def run():
    pTime = 0
    cTime = 0
    # Setting up the camera
    cap = cv2.VideoCapture(0)
    detector = htm.handDetector()

    while True:
        success, img = cap.read()
        img = detector.findHands(img, draw=False)
        lmList = detector.findPosition(img, draw=False)

        cTime = t.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, str(int(fps)), (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 0, 255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

        # Check if lmList is not empty before accessing its elements
        if lmList:
            print(lmList)
            if lmList[8] != 0:
                if lmList[8][1] != 0 and lmList[8][2] != 0:
                    print("moving bro")
                    pg.moveTo(lmList[8][1], lmList[8][2], 0.5, pg.easeOutQuad)
                    print("moved my bro")
            else:
                print("nahi no values")
