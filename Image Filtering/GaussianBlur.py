#blurred_image=cv2.GaussianBiur(img,(kernal_size_x,kernal_size_y),sigma)
#helps in image smoothening ,noise blur also used for preporcessing
import cv2

img = cv2.imread("image.png")
blurred = cv2.GaussianBlur(img, (5, 5), 4)
#Definition: The kernel is a small matrix (window) that moves over the image to apply the Gaussian function.
#In OpenCV: (kernel_size_x, kernel_size_y) → width × height of the kernel.
#--Kernel Size	Effect
#(3,3)	Slight blur
#(5,5)	Moderate blur
#(9,9)	Heavy blur
#in gaussian blur a kernal window all pixels are taken ad the average of their pixel is calculated
#then all values are replaced by avg value 
cv2.imshow("Original", img)
cv2.imshow("Blurred", blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
