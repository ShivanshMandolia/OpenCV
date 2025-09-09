import cv2

# Read image
image = cv2.imread("image.png")   # put your image in same folder

# Show image in a window
cv2.imshow("My Image", image)

# Wait until key is pressed
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()
