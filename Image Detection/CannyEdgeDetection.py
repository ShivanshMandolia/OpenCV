#edges=cv2.Canny(img,threshold1,threshold2)
#to  detect borderes,seperate objects,feature detection
'''
. What is Canny Edge Detection?

Its a popular algorithm to detect edges in an image.

Edges are places where the intensity changes sharply (like object boundaries).

How it works: Steps of the Canny algorithm
Step 1: Convert to grayscale

Edge detection works on intensity, so convert color images to grayscale.

Step 2: Noise reduction with Gaussian Blur

Blurring smooths the image and reduces noise that can cause false edges.

blurred = cv2.GaussianBlur(gray, (5,5), 1.4)

Step 3: Compute gradient intensity

Calculates change in intensity in horizontal (Gx) and vertical (Gy) directions using Sobel operator.

Gradient magnitude = sqrt(Gx^2 + Gy^2)

Gradient direction = arctan(Gy/Gx)

Step 4: Non-maximum suppression

Keeps only local maxima of the gradient.

Thin edges by removing pixels that are not at the maximum gradient in their direction.

Step 5: Double thresholding

Uses two thresholds: low and high

Strong edges → above high threshold

Weak edges → between low and high threshold

Below low → discarded

Step 6: Edge tracking by hysteresis

Weak edges are included only if they are connected to strong edges

Removes isolated weak edges (noise)
'''
import cv2

# Step 1: Read image in grayscale
img = cv2.imread("flower.jpg", cv2.IMREAD_GRAYSCALE)

# Step 2: Apply Gaussian Blur
blurred = cv2.GaussianBlur(img, (5, 5), 1.4)

# Step 3: Canny Edge Detection
#lower boundary 50 iske neche sare black and above 150 all are white 
edges = cv2.Canny(blurred, 50, 150)

# Step 4: Create a resizable window
cv2.namedWindow("Edges", cv2.WINDOW_NORMAL)

# Step 5: Resize window to very large size (e.g., 1200x800)
cv2.resizeWindow("Edges", 500, 500)

# Step 6: Show images
cv2.imshow("Original", img)
cv2.imshow("Edges", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
