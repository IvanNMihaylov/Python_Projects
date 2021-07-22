import cv2
import numpy as np

frameWidth = 640
frameHeight = 480

cap = cv2.VideoCapture(0)   # video if is 0 is the default camera

cap.set(3, frameWidth)      # set frame width
cap.set(4, frameHeight)     # se frame Height
cap.set(10, 100)            # set a brightness

# colors HSV (first 3 is a Min and other is Max )
myColors = [[157, 85, 0, 174, 246, 55],
            [85, 133, 0, 121, 255, 255],
            [11, 20, 229, 61, 111, 255]]

myColorValues = [[51, 153, 255],         # BGR colors
                 [255, 0, 255],
                 [0, 255, 0]]

myPoints = []  # [x, y, colorId]

def findColor(img, myColors, myColorValues):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    count = 0
    newPoints = []
    for color in myColors:
        lower = np.array(color[0:3])  # create array for lower
        upper = np.array(color[3:6])  # create array for upper
        mask = cv2.inRange(imgHSV, lower, upper)  # create mask to separate color
        x,y = getContours(mask)
        cv2.circle(imgResult, (x,y), 10, myColorValues[count], cv2.FILLED)   # where to see, center point, radius, color and filled
        if x != 0 and y != 0:
            newPoints.append([x, y, count])
        count += 1
        # cv2.imshow(str(color[0]), mask)
    return newPoints


def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    x,y,w,h = 0, 0, 0, 0
    for cnt in contours:
        area = cv2.contourArea(cnt)     # get area
        if area > 500:                  # check for trash area
            cv2.drawContours(imgResult, cnt, -1, (0, 0, 255), 3)    # drowing contours
            peri = cv2.arcLength(cnt, True)                         # arc lenght (или определяне на дължината на крива)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)         # get a points of shapes (x and y) len of that
            x, y, w, h = cv2.boundingRect(approx)                   # create bounding box (контур около обекта)

    return x+w//2, y    # center of the object (only for X)


def drowOnCanvas(myPoints, myColorValues):
    for point in myPoints:
        cv2.circle(imgResult, (point[0], point[1]), 10, myColorValues[point[2]], cv2.FILLED)

while True:
    success, img = cap.read()
    imgResult = img.copy()
    newPoints = findColor(img, myColors, myColorValues)
    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)
    if len(myPoints) != 0:
        drowOnCanvas(myPoints, myColorValues)
    cv2.imshow('Result', imgResult)
    if cv2.waitKey(1) & 0xFF == ord('q'):       #press 'q' for stop
        break

