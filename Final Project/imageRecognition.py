# import libraries
import cv2
import numpy as np
import glob
import pandas as pd

# Load image
def loadImage(filename):
    image = cv2.imread(filename)
    return image

def loadFolder(path):
    folder = glob.glob(path)
    return folder

def changeImage(image):
    # Convert image into gray scale
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the gray version of your image
    grayImageBlurred = cv2.blur(grayImg, (5,5))
    return grayImageBlurred

def showImage(title, image, seconds):
    # print out image
    cv2.imshow(title, image)
    # Close window after a certain amount of seconds
    # 0 = until program is stopped.
    cv2.waitKey(seconds)
    cv2.destroyAllWindow()


# Load, gray scale, and blur image
img = loadImage("img/eye.jpeg")
gib = changeImage(img)
# Apply Hough transform on the blurred image.
locatedCircles = cv2.HoughCircles(gib, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=50, minRadius=1, maxRadius=500)
# Only highlight detected circles if any circle is located in image
if locatedCircles is not None:
    locatedCircles = np.uint16(np.around(locatedCircles))
    for i in locatedCircles[0, :]:
        # Find middle and radius of circles
        middle = (i[0], i[1])
        radius = i[2]
        # Draw the outer ring around each circle
        cv2.circle(img, middle, radius, (0, 255, 0), 3)
        # Draw a dot or a circle with a radius of one in the center of each circle
        cv2.circle(img, middle, 1, (255, 0, 0), 3)

# Face detection using open CV libraries

cPath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cPath)

video_capture = cv2.VideoCapture(0)

while True:
    ret, webCam = video_capture.read()
    # faceImg = loadImage("img/ACDC.jpeg")
    grayFaceImg = changeImage(webCam)
    faces = faceCascade.detectMultiScale(grayFaceImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(webCam, (x, y), (x+w, y+h), (167, 200, 45), 2)
    #showImage("Faces", webCam, 0)
    cv2.imshow('Video', webCam)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
video_capture.release()
cv2.destroyAllWindows()

# Show image
# showImage("Eye", img, 0)

# Test for reading a folder
#maskFolder = loadFolder("./withMask/*.png")[75]
#singlePhoto = loadImage(maskFolder)
#showImage("test", singlePhoto, 0)
