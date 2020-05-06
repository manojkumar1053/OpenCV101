# M:\CV_PYIMAGE_SEARCh\1stEdition\1stEdition\Practical Python and OpenCV\code

# USAGE
# python load_display_save.py --image ../images/trex.png

# Import the necessary packages
import cv2

# Construct the argument parser and parse the arguments
img = "../images/test_images/trex.png"

# Load the image and show some basic information on it
image = cv2.imread(img)
# print(image)
print("width: %d pixels" % (image.shape[1]))
print("height: %d pixels" % (image.shape[0]))
print("channels: %d" % (image.shape[2]))

# Show the image and wait for a keypress
cv2.imshow("Image", image)
cv2.waitKey(0)

# Save the image -- OpenCV handles converting filetypes
# automatically
cv2.imwrite("newimage.jpg", image)
