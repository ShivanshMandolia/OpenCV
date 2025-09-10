#cv2.filter2D(src,ddepthj,kernel)->sharpens the feature outlines
import cv2
import numpy as np

# Step 1: Read the image
img = cv2.imread("image.png")

# Step 2: Define a sharpening kernel
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5, -1],#middle wlo ka influence bad diya as 5 hai
                           [0, -1, 0]])
                           #-1 matlab effect km kro 

# Step 3: Apply filter2D
sharpened = cv2.filter2D(img, -1, sharpen_kernel)
#d ddepth) refers to the data type of the pixels in an image, i.e., how many bits are used to represent each pixel value.
#ddepth → Depth of the output image
#If you use -1, the output image has the same depth as the input
# Step 4: Show images
cv2.imshow("Original", img)
cv2.imshow("Sharpened", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

