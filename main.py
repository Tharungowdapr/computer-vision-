import cv2

img = cv2.imread('sample.png')  # Replace with your image path

cv2.imshow('My Image', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
