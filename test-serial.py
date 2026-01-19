import serial
import time

#run this code and send one time "beep_number" via serial port to Arduino

# Replace 'COM9' with your actual port
arduino_port = '/dev/cu.usbserial-8010'
baud_rate = 115200

# Establish a serial connection with Arduino
ser = serial.Serial(arduino_port, baud_rate)
time.sleep(2)  # Wait for the connection to initialize

# Send the integer value as a string
beep_number = int(input("deg: "))
ser.write(f"{beep_number}\n".encode())

print("Blink delay sent to Arduino:", beep_number)

# Close the serial connection for 1 time communication
ser.close()
