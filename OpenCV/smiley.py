import numpy as np 
import cv2

canvas = np.zeros((300, 300, 3), dtype = "uint8")

green = (0, 255, 0)

cv2.line(canvas, (50, 200), (250, 200), green, 5)
cv2.rectangle(canvas, (60, 100), (80, 150), green, -1)
cv2.rectangle(canvas, (220, 100), (240, 150), green, -1)

cv2.imshow('Canvas', canvas)
cv2.waitKey(0)


