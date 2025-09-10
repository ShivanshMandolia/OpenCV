import cv2   # Import OpenCV library

# Step 1: Load Haar Cascade Classifiers
# Make sure all XML files are in the same folder as this script
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")  # Face detection
eye_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")                  # Eye detection
smile_cascade = cv2.CascadeClassifier("haarcascade_smile.xml")              # Smile detection

# Step 2: Start webcam capture (0 -> default webcam)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break  # Exit if no frame is captured

    # Convert each frame to grayscale (Haar works better with grayscale)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Step 4: Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # 1.3 -> scale factor, 5 -> minNeighbors

    for (x, y, w, h) in faces:
        # Draw rectangle around face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)

        # Add text "Face Detected" above rectangle
        cv2.putText(frame, "Face Detected", (x, y-10), cv2.FONT_HERSHEY_SIMPLEX,
                    0.8, (255, 0, 0), 2)

        # Extract region of interest (ROI) for eyes and smile within the face
        roi_gray = gray[y:y+h, x:x+w]      # Grayscale face region
        roi_color = frame[y:y+h, x:x+w]    # Color face region

        # Step 5: Detect eyes inside face ROI
        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 2)
            cv2.putText(roi_color, "Eye Detected", (ex, ey-5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 255, 0), 2)

        # Step 6: Detect smile inside face ROI
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)
        # 1.8 -> scaleFactor (higher because smile detection is harder)
        # 20 -> minNeighbors (increase to reduce false positives)

        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx+sw, sy+sh), (0, 0, 255), 2)
            cv2.putText(roi_color, "Smile Detected", (sx, sy-5), cv2.FONT_HERSHEY_SIMPLEX,
                        0.5, (0, 0, 255), 2)

    # Step 7: Show the output
    cv2.imshow("Webcam Face/Eye/Smile Detection", frame)

    # Exit on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Step 8: Release webcam and close windows
cap.release()
cv2.destroyAllWindows()
