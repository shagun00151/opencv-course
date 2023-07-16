# As we know that an image is made up of three channels BGR and opencv gives us the feature 
# to split the image into three channels.
import cv2 as cv
import numpy as np

img = cv.imread('park.jpg')
cv.imshow('Park', img)
blank = np.zeros(img.shape[:2], dtype='uint8')

b,g,r = cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Mergedimage',merged)

cv.waitKey(0)