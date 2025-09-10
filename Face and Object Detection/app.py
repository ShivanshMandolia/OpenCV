import cv2  

# Step 1: Load Haar Cascade Classifier
# Haar Cascade is a pre-trained XML file that contains data to detect objects (faces, eyes, etc.)
# OpenCV provides many ready-to-use Haar Cascades in cv2.data.haarcascades
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Step 2: Read input image
img = cv2.imread("person.png")   # Replace with your image path
# The algorithm works better on grayscale images, so we convert it
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Detect faces
# detectMultiScale() scans the image with different scales (zoom levels) to find faces
faces = face_cascade.detectMultiScale(
    gray,                # input image in grayscale
    scaleFactor=1.1,     # how much the image size is reduced at each scale (1.1 = 10% reduction)
    minNeighbors=5,      # how many neighbors a candidate rectangle should have to be considered a face
    minSize=(30, 30)     # ignore detections smaller than 30x30 pixels
)

# Step 4: Draw rectangles around detected faces
for (x, y, w, h) in faces:
    # (x,y) -> top-left corner of rectangle
    # (w,h) -> width and height of rectangle
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 3)  
    # Draw green rectangle with thickness 3

# Step 5: Display the result
cv2.imshow("Faces Detected", img)
cv2.waitKey(0)        # Wait for key press
cv2.destroyAllWindows()   # Close all windows
