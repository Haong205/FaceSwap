# This scrip will try to detect as much faces as possible from an image, then swap the faces around randomly

import random
import cv2

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

frameOG = cv2.imread('Assets/people.jpg', 1)
frameOG = cv2.resize(frameOG, (0, 0), fx=0.2, fy=0.2)
frame = frameOG.copy()

gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
faces_loc = face_cascade.detectMultiScale(gray, 1.3, 5)

faces = []
faces_index = []

# populate the list of faces
for (x, y, w, h) in faces_loc:
    face = frame[y:y + h, x:x + w].copy()
    faces.append(face)

# display each individual faces
for x, face in enumerate(faces):
    #cv2.imshow(str(x), face)
    faces_index.append(x)

# relocate each face randomly
for idx, (x, y, w, h) in enumerate(faces_loc):
    cv2.rectangle(frameOG, (x, y), (x + w, y + h), (255, 0, 0), 5)
    face_swap_idx = random.choice(faces_index)
    face_swap = faces[face_swap_idx]
    faces_index.remove(face_swap_idx)
    face_swap = cv2.resize(face_swap, (w, h))
    frame[y:y + h, x:x + w] = face_swap
    print(face_swap_idx)
    print(faces_index)

cv2.imshow('Original Image', frameOG)
cv2.imshow('Altered Faces', frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
