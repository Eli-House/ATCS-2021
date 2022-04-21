#import OpenCV
import cv2

#Load Image
cir = cv2.imread("img/Circle.png")

#print out image
cv2.imshow("Circle", cir)

#Close window aftter a certtain amoutt of seconds
# 0 = until program is stopped.
cv2.waitKey(0)
cv2.destroyAllWindow()