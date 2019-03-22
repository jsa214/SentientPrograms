# Capture an image when a face is detected in front of the 
# screen. Locate coordinates of face and paste face over 
# image.

import numpy as np 
import cv2

# Initialize 
haar_file = 'haarcascade_frontalface_default.xml'
data_set_size = 10


#'0' is used for my webcam,  
# if you've any other camera 
#  attached use '1' like this 
face_cascade = cv2.CascadeClassifier(haar_file) 
webcam = cv2.VideoCapture(0)  

# The program loops until it has 30 images of the face. 
count = 1
while count < data_set_size:  
    (_, im) = webcam.read() 
    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY) 
    faces = face_cascade.detectMultiScale(gray, 1.3, 4) 
    for (x, y, w, h) in faces: 
        cv2.rectangle(im, (x, y), (x + w, y + h), (255, 0, 0), 2) 
        face = gray[y:y + h, x:x + w] 
        face_resize = cv2.resize(face, (width, height)) 
        cv2.imwrite('% s/% s.png' % (path, count), face_resize) 
    count += 1

