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


# Show image
# showImage("Eye", img, 0)

# Test for reading a folder
maskFolder = loadFolder("./withMask/*.png")[75]
singlePhoto = loadImage(maskFolder)
showImage("test", singlePhoto, 0)
