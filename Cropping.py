import cv2

# Read image
image = cv2.imread("image.png") 

#cropped_image=image[startY:endY,startX:endX]
#we will do this using slicing ->when we want to extrACT ONLY A SMALL PART FROM BIG IMAGE
#image is a grid xaxis=colums(left to right) and siumilarly y axis (top to bottom)
cropped_image=image[20:100,30:70]
cv2.imshow("Cropped Image", cropped_image)

# Wait until key is pressed
cv2.waitKey(0)

# Close window
cv2.destroyAllWindows()
