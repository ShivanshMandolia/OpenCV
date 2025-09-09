#cv2.VideoWriter(filename,codec,fps,frame_size)
#.avi->audio video interleave for video and audio  storage 
#XVID codec->compression format,fps->frame/sec
#frame_size ->width and height
#step 1->open webcam 
#step 2->height and width of vid
#step 3->start recording 
#step 4->start saving and showing 
#step 5 ->press q and stop
import cv2

# Step 1: Open webcam
cap = cv2.VideoCapture(0)  # 0 = default webcam

# Step 2: Get height and width of the video frames
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)

# Step 3: Define the codec and create VideoWriter object
# 'XVID' codec, 20 fps, frame size same as webcam
out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, frame_size)

print("Recording started... Press 'q' to stop")

# Step 4: Start saving and showing frames
while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    out.write(frame)  # Save the frame to video file
    cv2.imshow("Webcam Recording", frame)  # Show live video

    # Step 5: Press 'q' to stop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Recording stopped")
        break

# Release everything
cap.release()
out.release()
cv2.destroyAllWindows()
