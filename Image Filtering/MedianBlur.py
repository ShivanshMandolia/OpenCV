#blurred=cv2.medianBlur(image,kernal_size)
import cv2

# Step 1: Read the image
image = cv2.imread("image.png")  # Replace with your image path

# Step 2: Apply median blur ->median value is taken and replaced instead of average 
# kernel_size must be an odd integer (3, 5, 7, ...)
kernel_size = 5
blurred = cv2.medianBlur(image, kernel_size)

# Step 3: Show original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Median Blurred Image", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()

'''
#Gaussian Blur
Smooths the image using a weighted average of surrounding pixels

Good for reducing general noise

Can blur edges slightly

Median Blur

Replaces each pixel with the median of its neighbors

Excellent for removing salt-and-pepper noise

Preserves edges better than Gaussian
'''
