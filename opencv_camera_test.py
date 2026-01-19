import cv2
import numpy as np
# Open the default camera (usually index 0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

print("Press 'q' to quit.")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # If frame is read correctly ret is True
    if not ret:
        print("Error: Can't receive frame (stream end?). Exiting ...")
        break
    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) 
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    filtered_image = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the resulting frame
    cv2.imshow('Camera Feed', filtered_image)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
