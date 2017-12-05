"""
This file provides helper functions
last modified 30-11-2017
"""

import cv2
import numpy as np
import shutil
import imutils
import os

def video2images(fn):
    """
    converts video to single images stored on disk
    :param fn: video stream file name
    :return: count, number of frames
    """
    dest = "/Users/TOSS/PycharmProjects/Detection/negatives"
    vidcap = cv2.VideoCapture(fn)
    success, image = vidcap.read()
    count = 0
    success = True
    #TODO: while loop not working correctly. Dreht eine Schleife zuviel. Abändern mit break
    while success:
        success, img = vidcap.read()
        if success == False:
            break
        height, width = img.shape[:2]
        res = cv2.resize(img, (int(width/4), int(height/4)), interpolation=cv2.INTER_AREA)
        cv2.imwrite(dest+"frame%d.jpg" % count, res)
        count += 1
    return count

def move2sample(nf, ns):
    """
    Sample frames to be used for the creation of positives
    :param nf: number of frames
    :param ns: number of samples
    :return: None
    """
    sample = np.random.choice(ns, nf, replace=False)
    source = "/Users/TOSS/PycharmProjects/Detection/frames/"
    dest = "/Users/TOSS/PycharmProjects/Detection/sample"
    for i in sample:
        #shutil.move(source + f, dest1)
        shutil.copy(source+"frame%d.jpg" % i,dest)

def main():
    fn = "/Users/TOSS/PycharmProjects/Detection/Video/VID_20171201_102006.mp4"
    numberofframes = video2images(fn)
    # numberofframes = 1828
    # move2sample(20, numberofframes)

if __name__ == "__main__":
    main()