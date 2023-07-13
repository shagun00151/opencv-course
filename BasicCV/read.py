# opencv is an libaray used for computer vision and caer is used to boost or speeding up.
# reading images
import cv2 as cv

img = cv.imread('cat_large.jpg')

cv.imshow('Cat', img)

cv.waitKey(0)

# reading videos
capture = cv.VideoCapture('dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
capture.release()
cv.destroyAllWindows()