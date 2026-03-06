from color_detection_hsv_prototype import getDonutCoordinate
import json
import time
import serial

port = '/dev/cu.usbserial-130'
baud_rate = 115200
ser = serial.Serial(port, int(baud_rate), timeout=2)

def goToServo(servopos):
    servo_data = servopos
    json_string = json.dumps(servo_data) + "\n"
    ser.write(json_string.encode("utf-8"))
    ser.flush()

foundDonut = False
gotDonut = False
donutPlaced = False
baseRot = 196
goToServo({"s0": 142, "s1": baseRot, "s2": 374})
time.sleep(1)
while True:
    if not foundDonut:
        goToServo({"s0": 142, "s1": baseRot, "s2": 374})
        cX, cY = getDonutCoordinate()
        if cX < 1020 and cX > 900:
            foundDonut = True
        baseRot += 5
    elif not gotDonut:
        s0 = 142
        while s0 < 540:
            goToServo({"s0": s0, "s1": baseRot, "s2": 374})
            s0 += 20
            time.sleep(0.5)
        goToServo({"s0": s0, "s1": baseRot, "s2": 100})
        time.sleep(0.5)
        s0 = 142
        goToServo({"s0": s0, "s1": baseRot, "s2": 100})
        gotDonut = True
    elif not donutPlaced:
        while baseRot < 540:
            goToServo({"s0": s0, "s1": baseRot, "s2": 100})
            baseRot += 5
            time.sleep(0.15)
        while s0 < 540:
            goToServo({"s0": s0, "s1": baseRot, "s2": 100})
            s0 += 20
            time.sleep(0.5)
        goToServo({"s0": s0, "s1": baseRot, "s2": 374})
    time.sleep(0.2)
    
    # print(getDonutCoordinate())