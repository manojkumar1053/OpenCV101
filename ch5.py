import cv2
import numpy as np

# img = "../images/test_images/trex.png"
# image = cv2.imread(img)
# print(image)
# cv2.imshow("Original", image)
# from numpy.core.tests.test_mem_overlap import xrange

canvas = np.zeros((300, 300, 3), dtype="uint8")
green = (0, 255, 0)
red = (0, 0, 255)
blue = (255, 0, 0)
yellow = (0, 255, 255)
cv2.line(canvas, (300, 0), (0, 300), red, 3)
cv2.line(canvas, (150, 0), (150, 300), blue, 5)
cv2.line(canvas, (0, 150), (300, 150), yellow, 7)
cv2.line(canvas, (0, 0), (300, 300), green, 9)

cv2.rectangle(canvas, (10, 10), (60, 60), green)
cv2.rectangle(canvas, (50, 200), (200, 225), red, 5)
# trying with negative values
cv2.rectangle(canvas, (200, 50), (225, 125), blue, -1)
# Drawing a circle
canvas = np.zeros((300, 300, 3), dtype="uint8")
(centerX, centerY) = (int(canvas.shape[1] / 2), int(canvas.shape[0] / 2))
white = [255, 255, 255]

for r in range(0, 175, 25):
    cv2.circle(canvas, (centerX, centerY), r, white, 5)
# cv2.imshow("Canvas", canvas)
# cv2.waitKey(0)

# Drawing Random Circle
for i in range(0, 26):
    radius = np.random.randint(5, 200)
    color = np.random.randint(0, 255, size=(3,)).tolist()
    pl = np.random.randint(0, 300, size=(2,))

    cv2.circle(canvas, tuple(pl), radius, color, -1)
cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
