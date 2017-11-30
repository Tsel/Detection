"""
This file provides helper functions
last modified 30-11-2017
"""

import cv2

def video2images(fn):
    vidcap = cv2.VideoCapture(fn)
    success, image = vidcap.read()
    count = 0
    success = True
    while success:
        success, image = vidcap.read()
        print('Read new frame: ', success)
        cv2.imwrite("frame%d.jpg" % count, image)
        count += 1