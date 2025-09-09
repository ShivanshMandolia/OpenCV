#cv2.rectangle(img,pt1,pt2,color,thickness)
#point1=top left corner and  pount2=bottom right

import cv2

# Read the image
img = cv2.imread("image.png")

# Draw rectangles
# Top-left at (50, 50), bottom-right at (200, 200)
rect1 = cv2.rectangle(img.copy(), (50, 50), (200, 200), (0, 255, 0), 3)

# Another filled rectangle
rect2 = cv2.rectangle(img.copy(), (100, 100), (300, 300), (255, 0, 0), -1)

# Show results
cv2.imshow("Rectangle with Border", rect1)
cv2.imshow("Filled Rectangle", rect2)

cv2.waitKey(0)
cv2.destroyAllWindows()
