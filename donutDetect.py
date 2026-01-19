import cv2
import numpy as np

# Global so mouse callback can see the latest frame
current_frame_lab = None
picked_color_lab = None
lMinMax, aMinMax, bMinMax = [], [], []


def getMouseEventLabColor(event, x, y, flags, param):
    global current_frame_lab, lMinmax, aMinMax, bMinMax
    if event == cv2.EVENT_LBUTTONDOWN and current_frame_lab is not None:
        # LAB at click position
        L, a, b2 = current_frame_lab[y, x]
        print(int(L), int(a), int(b2))
        lMinMax.append(int(L))
        aMinMax.append(int(a))
        bMinMax.append(int(b2))


cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Cannot open camera")
    raise SystemExit

cv2.namedWindow("frame")
cv2.setMouseCallback("frame", getMouseEventLabColor)

k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))

while True:
    ret, frame = cap.read()
    current_frame_lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

    if lMinMax and aMinMax and bMinMax:
        lower_lab = np.array([min(lMinMax), min(aMinMax), min(bMinMax)], dtype=np.uint8)
        upper_lab = np.array([max(lMinMax), max(aMinMax), max(bMinMax)], dtype=np.uint8)
    else:
        lower_lab = np.array([0, 0, 0], dtype=np.uint8)
        upper_lab = np.array([255, 255, 255], dtype=np.uint8)

    mask = cv2.inRange(current_frame_lab, lower_lab, upper_lab)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
