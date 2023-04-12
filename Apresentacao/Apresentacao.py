import cv2
import os
from cvzone.HandTrackingModule import HandDetector
import numpy as np

scale_percent = 47 # percent of original size
width = int(2730 * scale_percent / 100)
height = int(1480 * scale_percent / 100)
folderPath = 'Apresentar'

cap = cv2.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)
pathImages = sorted(os.listdir(folderPath), key=len)
# Variables
imgNumber = 0
hs, ws = int(120*1), int(213*1)
gestureThreshold = 400
buttonPressed = False
buttonCounter = 0
buttonDelay = 30
annotations = [[]]
annotationsNumber = 0
annotationStart = False

# Hand Detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    # Import Images
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.resize(cv2.imread(pathFullImage), (width, height),interpolation=cv2.INTER_AREA)

    hands, img = detector.findHands(img)
    cv2.line(img, (0, gestureThreshold), (width, gestureThreshold), (0,255, 0), 10)

    if hands and buttonPressed is False:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        #print(fingers)
        cx, cy = hand['center']
        lmList = hand['lmList']
        # Constrain values for easiest drawing
        xVal = int(np.interp(lmList[8][0], [width//2, width], [0, width]))
        yVal = int(np.interp(lmList[8][1], [150, height-150], [0, height]))
        indexFinger = xVal, yVal

        if cy <= gestureThreshold: # if hand have the height of the face
            annotationStart = False
            # Gesture 1 - Left
            if fingers == [1,0,0,0,0]:
                #print('left')
                annotationStart = False
                if imgNumber > 0:
                    annotations = [[]]
                    annotationsNumber = 0
                    buttonPressed = True
                    imgNumber -= 1
            
            # Gesture 2 - Right
            if fingers == [0,0,0,0,1]:
                #print('right')
                annotationStart = False
                if imgNumber < len(pathImages) - 1:
                    annotations = [[]]
                    annotationsNumber = 0
                    buttonPressed = True
                    imgNumber += 1

        # Gesture 3 - Show Pointer
        if fingers == [0, 1, 1, 0, 0]:
            cv2.circle(imgCurrent, indexFinger, 5, (0, 0, 255), cv2.FILLED)
            annotationStart = False

        # Gesture 4 - Draw Pointer
        if fingers == [0, 1, 0, 0, 0]:
            if annotationStart is False:
                annotationStart = True
                annotationsNumber += 1
                annotations.append([])
            cv2.circle(imgCurrent, indexFinger, 5, (0, 0, 255), cv2.FILLED)
            annotations[annotationsNumber].append(indexFinger)
        else:
            annotationStart = False

        # Gesture 5 - Erase
        if fingers == [0, 1, 1, 1, 0]:
            if annotations:
                if annotationsNumber >= 0:
                    annotations.pop(-1)
                    annotationsNumber -= 1
                    buttonPressed = True
    else:
        annotationStart = False

    # Button Pressed Iterations
    if buttonPressed:
        buttonCounter += 1
        if buttonCounter > buttonDelay:
            buttonCounter = 0
            buttonPressed = False
    
    # Loop through annotations
    for i in range(len(annotations)):
        for j in range(len(annotations[i])):
            if j != 0:
                cv2.line(imgCurrent, annotations[i][j - 1], annotations[i][j], (0 , 0, 200), 5)

    # Adding WebCam Image on the Slides
    imgSmall = cv2.resize(img, (ws,hs))
    h, w, _ = imgCurrent.shape
    # Direita
    # imgCurrent[0:hs, w-ws:w] = imgSmall
    # Esquerda
    imgCurrent[0:hs, 0:ws] = imgSmall
    #cv2.namedWindow('Slides', cv2.WINDOW_NORMAL)
    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break