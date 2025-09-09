#cv2.line(img,pt1,pt2,color,thickness)
#pt1=point 1 (start point ) pt2=point2 in (x,y)

import cv2

# Load your image
img = cv2.imread("image.png")

# Draw a line on the image
# Syntax: cv2.line(image, pt1, pt2, color, thickness)
cv2.line(img, (50, 50), (300, 50), (0, 0, 255), 4)   # Red horizontal line

# Show the image with the line
cv2.imshow("Image with Line", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
