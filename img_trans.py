#!/usr/bin/env
# -*- coding: utf-8 -

import cv2
import numpy as np

def image_resize(image, width = None, height = None, inter = cv2.INTER_AREA):
    # initialize the dimensions of the image to be resized and
    # grab the image size
    dim = None
    (h, w) = image.shape[:2]

    # if both the width and height are None, then return the
    # original image
    if width is None and height is None:
        return image

    # check to see if the width is None
    if width is None:
        # calculate the ratio of the height and construct the
        # dimensions
        r = height / float(h)
        dim = (int(w * r), height)

    # otherwise, the height is None
    else:
        # calculate the ratio of the width and construct the
        # dimensions
        r = width / float(w)
        dim = (width, int(h * r))

    # resize the image
    resized = cv2.resize(image, dim, interpolation = inter)

    # return the resized image
    return resized

img = cv2.imread("cooler.jpeg")
img = image_resize(img, height = 600)

dimensions =img.shape
print(dimensions)

cv2.circle(img, (2, 20), 5, (0, 0, 255), -1)
cv2.circle(img, (445, 8), 5, (0, 0, 255), -1)
cv2.circle(img, (120, 360), 5, (0, 0, 255), -1)
cv2.circle(img, (355, 362), 5, (0, 0, 255), -1)

pts1 = np.float32([[2, 20], [445, 8], [120, 360], [355, 362]])
pts2 = np.float32([[0, 0], [600, 0], [0, 700], [600, 700]])

matrix = cv2.getPerspectiveTransform(pts1, pts2)
result = cv2.warpPerspective(img, matrix, (600, 700))

cv2.imshow("Original", img)
cv2.imshow("transformed", result)

key = cv2.waitKey(0)



















