from __future__ import print_function
import sys
import cv2
from random import randint

cap = cv2.VideoCapture('vehicles.avi')
ret, frame = cap.read()

boxes = []
color = []
print("Draw box on the vehicles which is to be tracked ")
print("Press Enter key")
while True:
    box = cv2.selectROI('Tracker',frame)
    boxes.append(box)
    color.append((randint(0,255),randint(0,255),randint(0,255),randint(0,255)))

    print("Press q to quit selecting boxes and start tracking")
    print("Press any other key to select next object")
    k = cv2.waitKey(0) & 0xFF
    if (k == 113):
        break
print('Selected bounding boxes {}'.format(boxes))
#trackertype = cv2.TrackerCSRT_create()
multiTracker = cv2.MultiTracker_create()
for box in boxes:
    multiTracker.add(cv2.TrackerCSRT_create(), frame, box)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    ret, bboxes = multiTracker.update(frame)
    print("Press Esc to exit")
    for i, newbox in enumerate(bboxes):
        p1 = (int(newbox[0]), int(newbox[1]))
        p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
        cv2.rectangle(frame, p1, p2, color[i],2,1)

    cv2.imshow('Tracker',frame)

    if cv2.waitKey(1) & 0xFF == 27:

        break








