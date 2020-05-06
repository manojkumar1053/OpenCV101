# USAGE
# python getting_and_setting.py --image ../images/trex.png

# Import the necessary packages
import cv2

# Construct the argument parser and parse the arguments

img = "../images/test_images/trex.png"

# Load the image and show some basic information on it
image = cv2.imread(img)
# print(image)
cv2.imshow("Original", image)

# Images are just NumPy arrays. The top-left pixel can be
# found at (0, 0)

print(image[0, 0])
(b, g, r) = image[0, 0]
# color intensity at co-ordinate
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

# Now, let's change the value of the pixel at (0, 0) and
# make it red
image[0, 0] = (0, 0, 255)
(b, g, r) = image[0, 0]
print("Pixel at (0, 0) - Red: %d, Green: %d, Blue: %d" % (r, g, b))

# Since we are using NumPy arrays, we can apply slicing and
# grab large chunks of the image. Let's grab the top-left
# corner
corner = image[0:100, 0:100]
print("XXXXXXXXXXXXXX")
cv2.imshow("Corner", corner)

# Let's make the top-left corner of the image green
image[0:100, 0:100] = (0, 255, 0)

# Show our updated image
cv2.imshow("Updated", image)
cv2.waitKey(0)
