import serial
import time

# 👇 change the port if needed (try the other one if this fails)
port = '/dev/tty.usbmodemSN234567892'
baud = 9600

time.sleep(1)  # small delay before connecting
ser = serial.Serial(port, baud)
print("Serial port opened")

time.sleep(2)  # wait for Arduino reset

ser.write(b"Hello\n")
print("Data sent")

# read for 5 seconds
timeout = time.time() + 5
while time.time() < timeout:
    while ser.in_waiting > 0:
        line = ser.readline().decode().strip()
        print("Arduino says:", line)

ser.close()
print("Serial port closed")
