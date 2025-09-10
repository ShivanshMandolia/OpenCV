#merge->or   if u want to remove common ->and 
"""
1. cv2.bitwise_and(src1, src2, mask=None)

Performs a bitwise AND between two images.

Only pixels where both src1 and src2 are non-zero remain non-zero.

Often used with a mask to extract regions of interest.

2. cv2.bitwise_or(src1, src2, mask=None)

Performs a bitwise OR.

Pixels that are non-zero in either image remain non-zero.

Useful to combine images.

3. cv2.bitwise_xor(src1, src2, mask=None)

Performs a bitwise XOR.

Only pixels that are non-zero in one image but not both remain non-zero.

4. cv2.bitwise_not(src, mask=None)

Performs a bitwise NOT, i.e., inverts the pixel values.

Black becomes white, white becomes black.

5. Using a mask

Masks are grayscale images (same size as source) where 0 = ignore and 255 = keep.

Example of applying a mask with bitwise_and:


"""
import cv2
import numpy as np

# Create two black images of size 300x300
img1 = np.zeros((300, 300), dtype=np.uint8)
img2 = np.zeros((300, 300), dtype=np.uint8)

# Draw a white rectangle in img1
cv2.rectangle(img1, (100,100), (250, 250), 255, -1)  # filled rectangle

# Draw a white circle in img2
cv2.circle(img2, (150, 150), 100, 255, -1)  # filled circle

# Perform bitwise operations
bitwise_and = cv2.bitwise_and(img1, img2)
bitwise_or = cv2.bitwise_or(img1, img2)
bitwise_xor = cv2.bitwise_xor(img1, img2)
bitwise_not_img1 = cv2.bitwise_not(img1)
bitwise_not_img2 = cv2.bitwise_not(img2)

# Display all images
cv2.imshow("Image 1 - Rectangle", img1)
cv2.imshow("Image 2 - Circle", img2)
cv2.imshow("Bitwise AND", bitwise_and)
cv2.imshow("Bitwise OR", bitwise_or)
cv2.imshow("Bitwise XOR", bitwise_xor)
cv2.imshow("Bitwise NOT Image1", bitwise_not_img1)
cv2.imshow("Bitwise NOT Image2", bitwise_not_img2)

cv2.waitKey(0)
cv2.destroyAllWindows()
