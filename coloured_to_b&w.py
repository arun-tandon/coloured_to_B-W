import cv2
import numpy as np
img=cv2.imread("img.jpg")
output = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('B&W',output)

cv2.imwrite('B&W.png',output)
