from cvzone.HandTrackingModule import HandDetector
import cv2
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
detector = HandDetector(detectionCon=0.7, maxHands=2)
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img,flipType=True)  # With Draw
    cv2.rectangle(img, (0, 0), (250, 100), (0, 0, 0), -1)
    cv2.putText(img,
                'Click here to ',
                (0, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)
    cv2.putText(img,
                'play the game',
                (0, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1,
                (0, 255, 255),
                2,
                cv2.LINE_4)
    if len(hands) == 1:
            hand1 = hands [0]
            # print(hand1)
            lmList1 = hand1 ["lmList"]  # List of 21 Landmarks points
            bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
            centerPoint1 = hand1 ["center"]  # center of the hand cx,cy
            handType1 = hand1["type"]  # Hand Type Left or Right


            fingers1 = detector.fingersUp(hand1)

            if fingers1 == [1, 1, 1, 0, 0] or fingers1 == [0, 1, 1, 0, 0] :

                    length, info, img=detector.findDistance(lmList1[8], lmList1[12],img)
                    if length < 25:

                        if lmList1[8][1] <= 100 and lmList1[8][0] <= 255:
                            print('inside')
                            break
    cv2.imshow("Image",img)
    cv2.waitKey(1)
cap.release()
# close all windows
cv2.destroyAllWindows()