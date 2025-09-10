#threshold_value=cv2.threshold(img,thresh_bal,max_val,method)
'''The cv2.threshold() function is used for image binarization—converting a grayscale image into a 
black-and-white image based on a threshold.

Parameter	Description
src	      Input image (grayscale)
thresh	   Threshold value
maxval	   Maximum value assigned to pixels exceeding threshold
type	  Thresholding type (how pixels are compared to threshold)

cv2.THRESH_BINARY

if pixel > thresh: pixel = maxval
else: pixel = 0


cv2.THRESH_BINARY_INV

if pixel > thresh: pixel = 0
else: pixel = maxval


cv2.THRESH_TRUNC

if pixel > thresh: pixel = thresh
else: pixel = pixel

'''
import cv2

# Load image in grayscale
img = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)

# Apply simple binary threshold
thresh_value = 127
max_val = 255
retval, thresh_img = cv2.threshold(img, thresh_value, max_val, cv2.THRESH_BINARY)
cv2.namedWindow("Original", cv2.WINDOW_NORMAL)
cv2.namedWindow("Thresholded", cv2.WINDOW_NORMAL)

cv2.imshow("Original", img)
cv2.imshow("Thresholded", thresh_img)
cv2.resizeWindow("Original", 600, 400)       # resize window width x height
cv2.resizeWindow("Thresholded", 600, 400)
cv2.waitKey(0)
cv2.destroyAllWindows()
#Image should be gray scale and we can try thrshold 100,120,150
