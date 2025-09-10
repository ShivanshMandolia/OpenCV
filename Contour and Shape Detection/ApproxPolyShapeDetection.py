#approax=cv2.approxPolyDp(contour,epsilon,true)
#epsilon->small->precise ,large->rogh output(for small no of pooints)

import cv2

# Step 1: Read the input image
img = cv2.imread("circle.png")

# Step 2: Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Step 3: Apply thresholding
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Step 4: Find contours
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Step 5: Loop through each contour
for contour in contours:
    # Calculate contour perimeter (arc length)
    peri = cv2.arcLength(contour, True)  
    # arcLength(contour, True) -> True means contour is closed
    
    # Approximate the contour shape
    epsilon = 0.002 * peri  
    # epsilon = max distance from contour to approximated curve
    # small epsilon -> very precise, many points
    # large epsilon -> rough, fewer points
    
    approx = cv2.approxPolyDP(contour, epsilon, True)  
    # contour -> input contour
    # epsilon -> approximation accuracy
    # True -> indicates that the curve is closed
    
    # Draw the approximated contour on image
    cv2.drawContours(img, [approx], -1, (0, 0, 255), 3)  
    # Draw in red color with thickness 3
    
    # Optional: Label shape with number of sides
    #ravel cobvert multi d array into 1 d array and we will access first elementy 
    x, y = approx.ravel()[0], approx.ravel()[1]  # First vertex for placing text
    cv2.putText(img, f"Sides:{len(approx)}", (x, y), cv2.FONT_HERSHEY_SIMPLEX, 
                0.7, (255, 0, 0), 2)
    # len(approx) -> number of vertices in approximated polygon

# Step 6: Show the output
cv2.imshow("Approximated Contours", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
