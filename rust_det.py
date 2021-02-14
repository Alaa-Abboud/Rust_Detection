#!/usr/bin/env
# -*- coding: utf-8 -

import cv2
import numpy as np

# 9x9 median filtering
img = cv2.imread('transformed_screenshot.png')
filtered_img = cv2.medianBlur(img, 9)

# Convert BGR to HSV
hsv = cv2.cvtColor(filtered_img, cv2.COLOR_BGR2HSV)

# define range of reddish rust color spectrum in HSV 160-180 and 0-20
lower_red = np.array([0,50,50])
upper_red = np.array([11,255,255])
lower_red2 = np.array([175,50,50])
upper_red2 = np.array([179,255,255])

# Threshold the HSV image to get only red colors
mask1 = cv2.inRange(hsv, lower_red, upper_red)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask=mask1+mask2
ret,maskbin = cv2.threshold(mask,
127,255,cv2.THRESH_BINARY)

#calculate the percentage
height, width = maskbin.shape
size = height * width
percentage = cv2.countNonZero(maskbin)/float(size)
# Threshold percentage based on literature.
if percentage > 0.003:
 print ('rust-defected')
else:
 print ('not rusty')


