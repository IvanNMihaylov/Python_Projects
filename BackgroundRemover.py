import cv2
import cvzone
from cvzone.SelfiSegmentationModule import SelfiSegmentation
import os


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)
cap.set(cv2.CAP_PROP_FPS, 80)
segmenter = SelfiSegmentation()
fpsReader = cvzone.FPS()
# imgBg = cv2.imread("images/1.jpg")

listImg = os.listdir("images") #directory with images
print(listImg)
imgList = []
for imgPath in listImg:
    img = cv2.imread(f'images/{imgPath}')
    imgList.append(img)
print(len(imgList))

indexImg = 0

while True:
    success, img = cap.read()
    imageOut = segmenter.removeBG(img, imgList[indexImg], threshold=0.7) # remove background and putting a image

    imgStacked = cvzone.stackImages([img, imageOut], 2, 1)  #stack 2 images
    _, mgStacked = fpsReader.update(imgStacked, color=(0, 0, 255))

    # cv2.imshow("Image", img)
    cv2.imshow("Image", imgStacked)
    key = cv2.waitKey(1)

    #for change image background press 'a' or 'd' for quit a program press 'q'
    if key == ord('a'):
        if indexImg > 0:
            indexImg -= 1
    elif key == ord('d'):
        if indexImg < len(imgList)-1:
            indexImg += 1
    elif key == ord('q'):
        break

