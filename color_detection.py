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
    yellow_lower = np.array([20, 100, 100])  # Lower boundary for yellow in HSV
    yellow_upper = np.array([30, 255, 255])  # Upper boundary for yellow in HSV
    mask = cv2.inRange(hsv_image, yellow_lower, yellow_upper)
    

    height, width, _ = frame.shape
    #print(height, width)
    #center_y = height//2
    #center_x = width//2 
    #print(frame[center_x,center_y])
    #cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)
    # remove noise from mask. some how?
    mask = cv2.medianBlur(mask, 5) 
    M = cv2.moments(mask)
    cX = 0 
    cY = 0
    if M['m00'] != 0: # Avoid ZeroDivisionError
        cX = int(M['m10'] / M['m00'])
        cY = int(M['m01'] / M['m00'])
    mask = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    cv2.line(mask, (cX, 0), (cX, height), (0, 255, 0), 3)
    cv2.line(mask, (0, cY), (width, cY) , (0, 255, 0), 3)
    cv2.imshow('Camera Feed', mask)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
