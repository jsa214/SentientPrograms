# Capture an image when a face is detected in front of the 
# screen. Locate coordinates of face and paste face over 
# image.

import numpy as np 
import cv2
import random
import imutils

# Initialize 
haar_file = 'haarcascade_frontalface_default.xml'   # XML to train Cascade
(width, height) = (130, 100)                        # defining the size of images
fshrinkX = 25                                       # Number of pixels to constrain face detected region in the x direction
fshrinkY = 5                                        # Number of pixels to constrain face detected region in the x direction
outputImg_X = 1300
outputImg_Y = 1000

# Initialize Camera feed and cascade classifier
face_cascade = cv2.CascadeClassifier(haar_file) 
webcam = cv2.VideoCapture(0)  

# Quick webcam test to get image dimensions
(_, im) = webcam.read()
OrigHeight, OrigWidth, channels = im.shape
print("webcam input hieght: ", OrigHeight)
print("webcam input width: ", OrigWidth)

def createFaceGrid():
    # Collect an image of the user's face that they like
    userApproved = False
    while not userApproved:
        (_, im) = webcam.read() 
        print("Okay the code is buggy so once the window pops up, just click X after having a good look at it")
        cv2.imshow("Original", im)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        response = input("Continue with this image?(Y/N):")
        if((response=="Y") or (response=="y")):
            userApproved = True
        else:
            input("Retaking picture...press enter to continue")

    # Detect face and Confirm again with user
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
    for (x, y, w, h) in faces: 
        newYtop = y + fshrinkY
        newYbotton = y - fshrinkY
        newXleft = x + fshrinkX
        newXright = x - fshrinkX
        face = gray[(newYtop):(newYbotton + h), (newXleft):(newXright+ w)] 
        face_resize = cv2.resize(face, (width, height)) 

    # Show colorized and gray images
    cv2.imshow("image", face_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    colorFace = im[(newYtop):(newYbotton + h), (newXleft):(newXright+ w)]
    colorFace_resize = cv2.resize(colorFace, (width, height))
    colorFaceHeight, colorFaceWidth, channels = colorFace_resize.shape
    print("Original height: ", colorFaceHeight)
    print("Original Width: ", colorFaceWidth)
    cv2.imshow("image", colorFace_resize)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    # #Rotate face 360 degrees for giggles
    # for angle in np.arange(0,360,15):
    #     rotatedIm = imutils.rotate_bound(colorFace_resize, angle)
    #     rotatedHeight, rotatedwidth, channels = rotatedIm.shape
    #     print("Rotated height: ", rotatedHeight)
    #     print("Rotated Width: ", rotatedwidth)
    #     cv2.imshow("rotatedIm", rotatedIm)
    #     cv2.waitKey(0)
    #     cv2.destroyAllWindows()

    # Paste face all over image
    im = cv2.resize(im, (outputImg_X, outputImg_Y))
    for X_off in range(0, 10):
        for Y_off in range(0, 10):
            im[(Y_off*height):(Y_off*height + height), (X_off*width):(X_off*width + width)] = colorFace_resize
    cv2.imshow("image", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

     # Add in random rotated Images
    im = cv2.resize(im, (outputImg_X, outputImg_Y))
    for count in range(0, 500):
        Y_off_rand = random.randint(0, 9)
        X_off_rand = random.randint(0, 9)
        angle = random.randint(30, 330)
        rotatedIm = imutils.rotate_bound(colorFace_resize, angle)
        rotatedIm = cv2.resize(rotatedIm, (width, height))
        im[(Y_off_rand*height):(Y_off_rand*height + height), (X_off_rand*width):(X_off_rand*width + width)] = colorFace_resize
        im[(Y_off_rand*height):(Y_off_rand*height + height), (X_off_rand*width):(X_off_rand*width + width)] = rotatedIm

    cv2.imshow("image", im)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def FaceGrid():
    # Loop until user is done 
    UserSatisfied = False
    while not UserSatisfied:
        createFaceGrid()
        response = input("Are You Satisfied?(Y/N):")
        if((response=="Y") or (response=="y")):
            UserSatisfied = True
        else:
            input("Retaking then you narcissist")

FaceGrid()








