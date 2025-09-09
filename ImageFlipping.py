#flipped=cv2.flip(image,flipcode)
#flipcode=0->flip vertically (top to bittom)
#flipcode=1->horizontally
#flipcode=-1->both

import cv2

# Read the image
image = cv2.imread("image.png")

if image is None:
    print("Error: Image not found. Check the file path.")
else:
    flip_vertical = cv2.flip(image, 0)

    flip_horizontal = cv2.flip(image, 1)

    flip_both = cv2.flip(image, -1)

    # Show all images
    cv2.imshow("Original", image)
    cv2.imshow("Vertical Flip (0)", flip_vertical)
    cv2.imshow("Horizontal Flip (1)", flip_horizontal)
    cv2.imshow("Both Flip (-1)", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
