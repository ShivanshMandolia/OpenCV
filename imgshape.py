import cv2

# Read image
image = cv2.imread("image.png") 

#this will give 3 variable height ,width,color channels
h,w,c=image.shape
print(h,w,c)