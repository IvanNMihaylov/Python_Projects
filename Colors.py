import cv2
import cvzone
import numpy as np

def empty(a):   # func for create Track Bar
    pass


path = "-------"  # image directory
cv2.namedWindow("TrackBars")                                     # window for Track Bar (640x240)
cv2.resizeWindow("TrackBars", 640, 240)

# create a Trace Bar for Hue, Saturation and Value
cv2.createTrackbar("Hue Min", "TrackBars", 0, 178, empty)
cv2.createTrackbar("Hue Max", "TrackBars", 72, 178, empty)
cv2.createTrackbar("Sat Min", "TrackBars", 24, 255, empty)
cv2.createTrackbar("Sat Max", "TrackBars", 255, 255, empty)
cv2.createTrackbar("Val Min", "TrackBars", 52, 255, empty)
cv2.createTrackbar("val Max", "TrackBars", 255, 255, empty)

while True:
    img = cv2.imread(path)  # read a image
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  # HSV image (Hue Saturation Value)

    h_min = cv2.getTrackbarPos("Hue Min", "TrackBars")  # get track bars position
    h_max = cv2.getTrackbarPos("Hue Max", "TrackBars")
    s_min = cv2.getTrackbarPos("Sat Min", "TrackBars")
    s_max = cv2.getTrackbarPos("Sat Max", "TrackBars")
    v_min = cv2.getTrackbarPos("Val Min", "TrackBars")
    v_max = cv2.getTrackbarPos("val Max", "TrackBars")

    print(h_min, h_max, s_min, s_max, v_min, v_max)     # print value from track bar position
    lower = np.array([h_min, s_min, v_min])             # create array for lower
    upper = np.array([h_max, s_max, v_max])             # create array for upper
    mask = cv2.inRange(imgHSV, lower, upper)            # create mask to separate color
    imgResult = cv2.bitwise_and(img, img, mask=mask)    # to see the actual color for the mask

    imgStacked = cvzone.stackImages([img, imgHSV, mask, imgResult], 2, 2)   # stacked all images

    # cv2.imshow("Original", img)
    # cv2.imshow("HSV", imgHSV)
    # cv2.imshow("Mask", mask)
    # cv2.imshow("ImageResult", imgResult)
    cv2.imshow("Stacked", imgStacked)   # show images
    cv2.waitKey(0)

