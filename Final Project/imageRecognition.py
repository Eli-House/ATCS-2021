''' Eli Housenbold, ATCS-2021 Final Project, Face Mask Detection, May 10th 2021 '''
# import libraries
import cv2
import glob

# Load image
def loadImage(filename):
    image = cv2.imread(filename)
    return image

# Turn folder of photos into an array
# https://docs.python.org/3/library/glob.html
def loadFolder(path):
    folder = glob.glob(path)
    return folder

# Alter image for better detection
# https://docs.opencv.org/3.4/d4/d86/group__imgproc__filter.html#ga8c45db9afe636703801b0b2e440fce37
def changeImage(image):
    # Convert image into gray scale
    grayImg = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Blur the gray version of your image
    grayImageBlurred = cv2.blur(grayImg, (5,5))
    return grayImageBlurred

# Print out image with a title and duration
def showImage(title, image, seconds):
    # print out image
    cv2.imshow(title, image)
    # Close window after a certain amount of seconds
    # 0 = until program is stopped.
    cv2.waitKey(seconds)
    cv2.destroyAllWindow()

''' Mask Detection '''
# Call the pretrained face and eye detections from open cv
# Git hubs for the pretrained models
# https://github.com/shantnu/FaceDetect
# https://github.com/opencv/opencv/tree/master
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
eyeCascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Load, modify, and detect faces on an uploaded image
# faceImg = loadImage("img/ACDC.jpeg")
# grayFaceImg = changeImage(faceImg)
# faces = faceCascade.detectMultiScale(grayFaceImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Draw rectangles around faces and show an uploaded image
#for (x, y, w, h) in faces:
    #cv2.rectangle(faceImg, (x, y), (x+w, y+h), (167, 200, 45), 2)
#showImage("Find Faces", faceImg, 0)

''' Video Mask Detection'''
# Begin the vide on the webcam
videoCapture = cv2.VideoCapture(0)
while True:
    # Read the data from the webcam
    ret, webCam = videoCapture.read()
    # Turn the image gray and blur it for more accurate detection
    grayFaceImg = changeImage(webCam)
    # Detect Eyes and faces from the live video on the webcam
    faces = faceCascade.detectMultiScale(grayFaceImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    eyes = eyeCascade.detectMultiScale(grayFaceImg, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected eyes
    for (x, y, w, h) in eyes:
        # Draw a green rectangle at the location of the detected eye
        cv2.rectangle(webCam, (x, y), (x+w, y+h), (0, 255, 0), 2)

    for (x, y, w, h) in faces:
        # Draw a red rectangle at the location of the detected face
        cv2.rectangle(webCam, (x, y), (x+w, y+h), (0, 0, 255), 2)
        # Print out text that says no mask on top of the face detected box
        # https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
        webCam = cv2.putText(webCam, 'No Mask', (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
        # Isolate the pixels inside the face detected box
        eyeGray = grayFaceImg[y:y+h, x:x+w]
        eyeColor = webCam[y:y+h, x:x+w]
        # Recall eye detection but inside the face detection box
        eyes = eyeCascade.detectMultiScale(eyeGray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        for (eyesX, eyesY, eyesW, eyesH) in eyes:
            # Draw a red rectangle at the location of the detected eye
            cv2.rectangle(eyeColor, (eyesX, eyesY), (eyesX+eyesW, eyesY+eyesH), (0, 0, 255), 2)

    # Shows the webCam Photo. My method for showing images only works for pictures and not video
    cv2.imshow('Mask?', webCam)

    # This line runs the while loop until the q key is pressed. The q key will quit the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Stop capturing video and destroy all windows
videoCapture.release()
cv2.destroyAllWindows()


# Test for reading a folder
#maskFolder = loadFolder("./withMask/*.png")[75]
#singlePhoto = loadImage(maskFolder)
#showImage("test", singlePhoto, 0)

''' Circle detection on Image
Help Citations:
https://docs.opencv.org/3.4/d4/d70/tutorial_hough_circle.html
'''

'''
# Load, gray scale, and blur image
img = loadImage("img/eye.jpeg")
gib = changeImage(img)

# Apply Hough transform on the blurred image inorder to detect circles.
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
'''