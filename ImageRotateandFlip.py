import cv2

# Read image
image = cv2.imread("image.png") 
#Rotate
#M=cv2.getRotationMatrix2D(center,angle,scale) scale =1.0 same saize 2.0 ->double 0.5->half
#rotated_image=cv2.wrapAffine(image,M,(width,height))
#for exact center of image centre point=(w//2,h//2) so first find hwight and width using shape


if image is None:
    print("Error: Image not found. Check the file path.")
else:
    # Get height, width of image
    (h, w) = image.shape[:2]
    center = (w // 2, h // 2)

    # Rotate +90 degrees, scale 0.5
    M1 = cv2.getRotationMatrix2D(center, 90, 0.5)
    rotated1 = cv2.warpAffine(image, M1, (w, h))

    # Rotate -180 degrees, scale 2.0
    M2 = cv2.getRotationMatrix2D(center, -180, 2.0)
    rotated2 = cv2.warpAffine(image, M2, (w, h))

    # Show images
    cv2.imshow("Original", image)
    cv2.imshow("Rotated +90, Scale 0.5", rotated1)
    cv2.imshow("Rotated -180, Scale 2.0", rotated2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
