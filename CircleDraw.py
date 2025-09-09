#cv2.circle(img,center,radius,color,thickness)
import cv2

# Read the image
img = cv2.imread("image.png")

# Copy for different examples
circle1 = img.copy()
circle2 = img.copy()

# Circle with border only
cv2.circle(circle1, (150, 150), 50, (0, 255, 0), 3)

# Filled circle
cv2.circle(circle2, (100, 200), 80, (255, 0, 0), -1)

# Show results
cv2.imshow("Circle with Border", circle1)
cv2.imshow("Filled Circle", circle2)

cv2.waitKey(0)
cv2.destroyAllWindows()
