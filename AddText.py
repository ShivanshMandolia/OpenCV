#cv2.putText(img,text,org,font,fontscale,color,thickenss) org=(x,y)
import cv2

# Read the image
img = cv2.imread("image.png")

# Put text
cv2.putText(img, "OpenCV Demo", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 
            2, (255, 0, 0), 2)

cv2.putText(img, "Hello World!", (50, 200), cv2.FONT_HERSHEY_COMPLEX, 
            1, (0, 255, 0), 2)

# Show image
cv2.imshow("Text Example", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
