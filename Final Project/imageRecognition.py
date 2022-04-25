# import libraries
import cv2
import numpy as np

# Load image
img = cv2.imread("img/multiCircles.jpeg")
#img = cv2.imread("img/eye.jpeg")
#img = cv2.imread("img/car.jpeg")
#img = cv2.imread("img/basketball.jpeg")


# Convert image into gray scale
gImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Blur image
gCirBlurred = cv2.blur(gImg, (5,5))

# Apply Hough transform on the blurred image.
locatedCircles = cv2.HoughCircles(gCirBlurred, cv2.HOUGH_GRADIENT, 1, 100, param1=100, param2=50, minRadius=1, maxRadius=500)

# Only highlight detected circles if any circle i located in image
if locatedCircles is not None:
    # Convert the circle parameters a, b and r to integers.
    locatedCircles = np.uint16(np.around(locatedCircles))
    for i in locatedCircles[0, :]:
        # Find middle and radius of circles
        middle = (i[0], i[1])
        radius = i[2]
        # Draw the outer ring around each circle
        cv2.circle(img, middle, radius, (0, 255, 0), 3)
        # Draw a dot or a circle with a radius of one in the center of each circle
        cv2.circle(img, middle, 1, (255, 0, 0), 3)

# print out image
cv2.imshow("Circle", img)

# Close window after a certain amount of seconds
# 0 = until program is stopped.
cv2.waitKey(0)
cv2.destroyAllWindow()

