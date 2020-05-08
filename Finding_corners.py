import numpy as np
import cv2
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#from skiimage import io

# prepare object points
nx = 8#TODO: enter the number of inside corners in x
ny = 6#TODO: enter the number of inside corners in y
#images
# Make a list of calibration images
fname = "C:\\Users\\manoj\\PycharmProjects\\untitled2\\images\\calibration_test.png"
img = cv2.imread(fname)
print(img)


#img1=cv2.cv.LoadImage(fname)
#print(img1,CV_LOAD_IMAGE_COLOR)


# Convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (nx, ny), None)
print(ret,corners)
# If found, draw corners
if ret == True:
    # Draw and display the corners
    cv2.drawChessboardCorners(img, (nx, ny), corners, ret)
    plt.imshow(img)
