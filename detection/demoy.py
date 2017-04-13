#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse
import os
import re
import sys
import cv2 as cv
from nms import nms
import numpy as np

cnt = 0;


def parsearguments():
    parser = argparse.ArgumentParser(description='object detection using cascade classifier')
    parser.add_argument('-i', '--image', help='image file name', default='/home/gongxijun/data')
    parser.add_argument('-c', '--cascade', dest='cascadefilename', help='cascade file name',
                        default='/home/gongxijun/data/lantern/data/model/cascade.xml')
    parser.add_argument('-s', '--scalefactor', dest='scalefactor', type=float, default=1.1)
    parser.add_argument('-m', '--minneighbors', dest='minneighbors', type=int, default=3)
    parser.add_argument('-o', '--output', dest='output',
                        default='box/detect.jpg')
    return parser.parse_args()


def detect(img, cascadefilename, scalefactor, minneighbors):
    global cnt
    srcimg = img
    if srcimg is None:
        print('cannot load image')
        sys.exit(-1)
    cascade = cv.CascadeClassifier(cascadefilename)
    # print cascade
    objects = cascade.detectMultiScale(srcimg, scalefactor, minneighbors)
    _num_status = True
    while _num_status and len(objects) > 0:
        objects, _num_status = nms(list(objects), 0.6)
    count = len(objects)
    if count > 0:
        cnt += 1;
    print('detection count: %s' % (count,))
    # print (objects)
    for (x, y, w, h) in (objects):
        # print(x, y, w, h)
        cv.rectangle(srcimg, (x, y), (x + w, y + h), (0, 0, 255), 2)
    return srcimg


args = parsearguments()
print('cascade file: %s' % (args.cascadefilename,))

def showImage(img):
    result=detect(img, args.cascadefilename,
           args.scalefactor, args.minneighbors)
    return result
