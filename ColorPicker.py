import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)   # video if is 0 is the default camera
cap.set(3, frameWidth)      # set frame width
cap.set(4, frameHeight)     # se frame Height
cap.set(10, 130)            # set a brightness


def empty(a):   # func for create Track Bar
    pass

cv2.namedWindow("HSV")
cv2.resizeWindow("HSV", 640, 240)
cv2.createTrackbar("Hue Min", "HSV", 0, 178, empty)
cv2.createTrackbar("Sat Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Val Min", "HSV", 0, 255, empty)
cv2.createTrackbar("Hue Max", "HSV", 178, 178, empty)
cv2.createTrackbar("Sat Max", "HSV", 255, 255, empty)
cv2.createTrackbar("val Max", "HSV", 255, 255, empty)


while True:
    _, img = cap.read()
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos("Hue Min", "HSV")  # get track bars position
    h_max = cv2.getTrackbarPos("Hue Max", "HSV")
    s_min = cv2.getTrackbarPos("Sat Min", "HSV")
    s_max = cv2.getTrackbarPos("Sat Max", "HSV")
    v_min = cv2.getTrackbarPos("Val Min", "HSV")
    v_max = cv2.getTrackbarPos("val Max", "HSV")

    lower = np.array([h_min, s_min, v_min])             # create array for lower
    upper = np.array([h_max, s_max, v_max])             # create array for upper
    mask = cv2.inRange(imgHSV, lower, upper)            # create mask to separate color
    result = cv2.bitwise_and(img, img, mask=mask)    # to see the actual color for the mask

    mask = cv2.cvtColor(mask, cv2.COLOR_BAYER_GR2BGR)
    hStack = np.hstack([img, mask, result])

    cv2.imshow("Horizontal Stacking", hStack)
    # cv2.imshow('Horizontal Stacking', img)
    # cv2.imshow('Horizontal Stacking', imgHSV)
    # cv2.imshow('Horizontal Stacking', mask)
    # cv2.imshow('Horizontal Stacking', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cap.release()
# cap.destroyAllWindows()
