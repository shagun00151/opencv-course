import cv2 as cv

img = cv.imread('cat.jpg')
cv.imshow('Cats',img)

# Averaging - it is the method of taking averageg of intensity of other 8 pixels in surrounding
# and result is given at middle
average = cv.blur(img,(3,3))
cv.imshow('Average',average)

# Gaussian blur method weights are assigned and its average is calculated for blurring it is 
# more natural than average and 0 in this case defines the standard deviation
gauss = cv.GaussianBlur(img,(3,3),0)
cv.imshow('Gaussian',gauss)

# Median blur is the method of taking median of intensity of other 8 pixels in surrounding.
# It is more effective in removing noise as compared to average and gaussian blur.
median = cv.medianBlur(img, 3)
cv.imshow('Median Blur', median)

# Bilateral is the most effective method of blurring as it keeps the edges sharp and removes
# noise.
bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)