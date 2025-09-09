import cv2

# Read image
image = cv2.imread("image.png")   # put your image in same folder
if image is not None:
    success=cv2.imwrite("image.png",image)
    if success:
        print("saved suceessfully")
    else:
        print("sorry error occur")