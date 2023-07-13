import cv2 as cv
img = cv.imread('cat.jpg')

cv.imshow('Cat',img)

# Converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

# converting image to blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('Blur',blur)

# Edge Cascade Detection
canny = cv.Canny(img,125,175)
cv.imshow('Canny Edges',canny)

# Dilating the image
# helps in making the edges thicker
dilate = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilated',dilate)

# eroding the image
eroded = cv.erode(dilate,(7,7),iterations=3)
cv.imshow('Eroded',eroded)

# Resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_AREA)
cv.imshow('Resized',resize)

# Cropping
cropped = img[50:200,200:400]
cv.imshow('Cropped',cropped)

cv.waitKey(0)