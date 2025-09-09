#In OpenCV, frame-by-frame processing means you capture each frame from a video
# (or webcam) and apply some image processing operations to it before displaying or saving it. 
import cv2

cap = cv2.VideoCapture(0)  # Open default webcam

while True:
    ret, frame = cap.read()  # Capture a frame
    if not ret:
        print("Could not read frame")
        break

    # 1. Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 2. Flip horizontally
    flipped = cv2.flip(frame, 1)  # 1 = horizontal flip

    # 3. Draw a rectangle and put text
    cv2.rectangle(flipped, (50, 50), (250, 150), (0, 255, 0), 3)  # green rectangle
    cv2.putText(flipped, "Webcam", (60, 120), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Display the processed frames
    cv2.imshow("Original Frame", frame)
    cv2.imshow("Grayscale Frame", gray)
    cv2.imshow("Flipped + Shapes Frame", flipped)

    if cv2.waitKey(1) & 0xFF == ord('q'):  # Press 'q' to quit
        break

cap.release()
cv2.destroyAllWindows()
