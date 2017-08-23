import cv2
import numpy as np

img = cv2.imread('watch1.jpg',cv2.IMREAD_COLOR)

cv2.line(img, (0,0), (150,150), (255,255,255), 15)

cv2.rectangle(img, (15,25), (200,150), (0,255,0), 5)

pts = np.array([10,5],[20],[])

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows
