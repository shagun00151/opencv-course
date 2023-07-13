# thresholding and binarizing is defined as the converting the image into binary number 
# on the basis of some threshold data below which the pixel value is 0 and above which 
# the pixel value is 1 or 255.

import cv2 as cv

img = cv.imread('cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold,thresh = cv.threshold(gray,100,255,cv.THRESH_BINARY)
cv.imshow('simple_threshold',thresh)

# this is basically the inverse of the threshold function.
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV )
cv.imshow('Simple Thresholded Inverse', thresh_inv)

# Adaptive Thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 9)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)