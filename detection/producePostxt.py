#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import argparse
import re
import os
import sqlite3
import sys
import codecs
from config import config as cf
from PIL import Image
from skimage import transform, color
import cv2 as cv


def produceNegTxt(filedirpath, imagedir, filename='neg.txt'):
    filedirpath = os.path.join(cf.pro_path, filedirpath);
    imagedir = os.path.join(cf.pro_path, imagedir);
    if not os.path.exists(filedirpath):
        os.makedirs(filedirpath)
    if not os.path.exists(imagedir):
        print 'image dir is not exists ~'
        sys.exit(-1)
    pattern = re.compile('.*[.](jpg|jpeg|png)$')
    images = [image for image in os.listdir(imagedir) if re.match(pattern, image)]
    with codecs.open(os.path.join(filedirpath, filename), 'w', encoding='utf-8') as fw:
        for i, image in enumerate(images):
            try:
                imagesrc = os.path.join(imagedir, images[i])
                os.rename(imagesrc, os.path.join(imagedir, 'neg_' + str(i + 1) + '.jpg'))
                print(imagesrc)
                fw.write('{}\n'.format(os.path.join('/neg', 'neg_' + str(i + 1) + '.jpg')));  # x,y,w,h,status
            except Exception, e:
                print  e


def producePosTxt(filedirpath, imagedir, filename='pos.txt'):
    filedirpath = os.path.join(cf.pro_path, filedirpath);
    imagedir = os.path.join(cf.pro_path, imagedir);
    if not os.path.exists(filedirpath):
        os.makedirs(filedirpath)
    if not os.path.exists(imagedir):
        print 'image dir is not exists ~'
        sys.exit(-1)
    pattern = re.compile('.*[.](jpg|jpeg|png)$')
    images = [image for image in os.listdir(imagedir) if re.match(pattern, image)]
    with codecs.open(os.path.join(filedirpath, filename), 'w', encoding='utf-8') as fw:
        for i, image in enumerate(images):
            try:
                imagesrc = os.path.join(imagedir, images[i])
                tmp_img = cv.imread(imagesrc)
                #tmp_img = transform.resize(tmp_img,(128,90));
                #cv.imwrite(imagesrc,tmp_img*255);
                #os.rename(imagesrc, os.path.join(imagedir, 'pos_' + str(i + 1) + '.jpg'))
                print(imagesrc)
                fw.write('{} {} {} {} {} {}\n'.format(imagesrc, 1, 0, 0,
                                                      tmp_img.shape[1],
                                                      tmp_img.shape[0],
                                                       1));  # status,x,y,w,h
            except Exception, e:
                print  e


if __name__ == '__main__':
    # produceNegTxt('data/image', 'data/image/neg')
    producePosTxt('data/image', 'data/image/pos')
