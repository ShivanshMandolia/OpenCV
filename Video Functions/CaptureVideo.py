import cv2
cap=cv2.VideoCapture(0)# put 0 inside when device camera 1 if external camera/webcam
while True:#for contnously reading frames
#cap.read captures a single frame from webcam returns two value bool ret and frame->numpy array
    ret,frame=cap.read()#ret=true/false frame=image
    if not ret:
        print("Could Not read  frame")
        break
    cv2.imshow("Webcam feed",frame)
    #cv2.waitKey(1) waits 1 millisecond for a key press.
#The bitwise & 0xFF ensures compatibility across platforms.
#ord('q') converts 'q' to its ASCII value.
#Effect: If you press 'q', the loop will stop.
    if cv2.waitKey(1)&0xFF==ord('q'):
        print("quitting..")
        break
        #release the webcam
cap.release()
cv2.destroyAllWindows()