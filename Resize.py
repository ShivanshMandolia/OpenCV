import cv2

# Read image
image = cv2.imread("image.png") 
#resized=cv2.resize(src,dsize,fx,fy,interpolation)
#dsize mai pehle aayegi  width then height
#fx,fy->scale factor and interpolation ->quality control bith are optiuona;l
if image is not None:
    resized=cv2.resize(image,(1000,300))
    cv2.imshow("Orig image",image)
    cv2.imshow("Resized image",resized)
    cv2.imwrite("resized_ouput.png",resized)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else :
    print("Image is not loaded")
