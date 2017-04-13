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


def detect(imagefilename, cascadefilename, scalefactor, minneighbors):
    global cnt
    srcimg = cv.imread(imagefilename)
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


if __name__ == '__main__':
    args = parsearguments()
    print('cascade file: %s' % (args.cascadefilename,))
    lists = ['/home/gongxijun/data/dataset/neg', '/home/gongxijun/data/222']
    imagedir = lists[-1]
    pattern = re.compile('.*[.](jpg|jpeg|png|bmp|gif)$')
    images = [image for image in os.listdir(imagedir) if re.match(pattern, image)]
    print('target files: %s' % (len(images),))
    for i, image in enumerate(images):
        imagesrc = os.path.join(imagedir, images[i])
        result = detect(imagesrc, args.cascadefilename,
                        args.scalefactor, args.minneighbors)
        dstfilename = './demo/detect_%s' % (images[i],)
        cv.imwrite(dstfilename, result)
        print '@@@@@@@@@@@@@@@@@@@@@ {}/{}'.format(cnt, i)
