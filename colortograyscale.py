import cv2

# Read image
image = cv2.imread("image.png") 
#convert color image to gray image 
if image is not None:
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    cv2.imshow("Gray Image", gray)

# Wait until key is pressed->luch bhi key krlenge press to close hojayega
    cv2.waitKey(0)

# Close window
    cv2.destroyAllWindows()
else:
    print("COuld not load image")