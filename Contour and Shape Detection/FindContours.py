"""
In computer vision (OpenCV), a contour is simply the curve or boundary that joins all the continuous points along the boundary of an object having the same intensity or color.

Think of it as the outline of a shape in an image.

A contour is represented as a list of points (x, y coordinates) in OpenCV.

Contours are very useful for shape analysis, object detection, and image segmentation.

For example:

If you have a white object on a black background, the contour would trace the edge of that white object.

OpenCV provides the function cv2.findContours() to detect contours.

Key Points

Contours are drawn around edges of objects.

They work best on binary images (after applying thresholding or edge detection).

Contours can be external (outer boundary) or hierarchical (boundaries inside boundaries).
"""
#work onm binary image (after cannny detection or thresholding )
#cont0ours,heiarchy=cv2.findcountours(img,mode,method)
#mode->retrival->how many contours and what kind of contours 
#mode=RET_EXTN->outermost shape and RET_TREE->all shapes with heiarchy RET_LIST->all shapes wthout heiarchyu

#method->how much detail to return on each contour
#chain approaax->corner point store ->shape detection
#chain approac none->every detail->handwriting detection

import cv2  

img = cv2.imread("shape.png")   # Reads the image from the file 'shape.png'
# img is by default read in BGR (Blue, Green, Red) format

# Step 2: Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  
# Contour detection works on binary (black/white) images
# Grayscale conversion reduces the image to a single channel

# Step 3: Apply thresholding to get binary image
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)  
# 200 -> threshold value
# 255 -> max value (white)
# THRESH_BINARY -> pixels >200 become 255 (white), others become 0 (black)
# '_' -> return value of threshold used (not required here)

# Step 4: Find contours from the binary image
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  
# contours -> list of all detected contours (each contour is a list of points)
# hierarchy -> information about relationship among contours
# cv2.RETR_TREE -> retrieves all contours and builds hierarchy
# cv2.CHAIN_APPROX_SIMPLE -> compresses points, stores only endpoints (saves memory)

# Step 5: Draw contours on the original image
cv2.drawContours(img, contours, -1, (0,255,0), 3)  
# img -> image on which contours will be drawn
# contours -> list of contours
# -1 -> draw all contours (-1 means ALL, 0 means only first contour, 1 means second, etc.)
# (0,255,0) -> color of contour in BGR (green here)
# 3 -> thickness of contour line

# Step 6: Show the results
cv2.imshow("Gray Image", gray)       # Show grayscale version
cv2.imshow("Threshold Image", thresh) # Show binary thresholded version
cv2.imshow("Contours", img)           # Show image with contours drawn

cv2.waitKey(0)   # Wait for any key press to close windows
cv2.destroyAllWindows()   # Close all windows after key press
