from os import error
import serial
from pynput.mouse import Controller
from variables import SerialInput, CursorSpeed

print(">>> Arduino-Joystick-Controller v-alpha")
print(">>> Please edit 'variables.py' to enter the relevant informations for your setup")

DEVICE_STARTED = 0x0
NO_ACCELEROMETER = 0xe0
ACCELEROMETER_DETECTED = 0xe1
X_ACCEL = 0x10
Y_ACCEL = 0x11
Z_ACCEL = 0x12
X_GYRO = 0x20
Y_GYRO = 0x21
Z_GYRO = 0x22
TEMP = 0x30

ser = serial.Serial(SerialInput, 9600)

print(">>> Connection established !")

mouse = Controller()

def recv(ser, opcode, mouse):

    """
    recv is the function that process the informations
    coming from the mpu6050 through the Arduino
    """

    if opcode == DEVICE_STARTED:
        print(">>> Device has started")
    elif opcode == NO_ACCELEROMETER:
        print(">>> No accelerometer detected")
    elif opcode == ACCELEROMETER_DETECTED:
        print(">>> Accelerometer detected")
    elif opcode == X_ACCEL:
        # Debug only
        print(ser.readline())
    elif opcode == Y_ACCEL:
        # Debug only
        print(ser.readline())
    elif opcode == Z_ACCEL:
        # Debug only
        print(ser.readline())
    elif opcode == X_GYRO:
        # Debug only
        print(ser.readline())
    elif opcode == Y_GYRO:
        v = float(ser.readline().rstrip())
        t = float(ser.readline().rstrip())
        mouse.move(0,int(CursorSpeed*(v*t/1000)))
    elif opcode == Z_GYRO:
        v = float(ser.readline().rstrip())
        t = float(ser.readline().rstrip())
        mouse.move(-int(CursorSpeed*v*t/1000),0)
    elif opcode == TEMP:
        # Debug only
        print(">>> Temperature")
        print(ser.readline())

while True:
    try:

        # Retrieve opcode
        data = ser.readline()
        opcode = int(data.rstrip())

        # Process opcode
        recv(ser, opcode, mouse)
    except Exception as e:
        print(e)