from os import error
import serial
#from pynput.keyboard import Controller

print("Hello Welcome to NBox 100")

print("""Please enter the COM port of your controller.
You can find it if you go to your device manager and look for COM & LPT
section. find your device by unpluging it and pluging it again.
You write it like:
ex: COM8
""")

sInput = "COM5"

ser = serial.Serial(sInput, 9600)

print("connection established")

#keyboard = Controller()
r = [0.0,0.0,0.0]

def recv(ser, opcode, r):
    if opcode == 0x0:
        print("Device has started")
    elif opcode == 0xe0:
        print("No accelerometer detected")
    elif opcode == 0xe1:
        print("Accelerometer detected")
    elif opcode == 0x10:
        print("X")
        print(ser.readline())
    elif opcode == 0x11:
        print("Y")
        print(ser.readline())
    elif opcode == 0x12:
        print("Z")
        print(ser.readline())
    elif opcode == 0x20:
        print("X")
        print(ser.readline())
    elif opcode == 0x21:
        v = float(ser.readline().rstrip())
        t = float(ser.readline().rstrip())
        r[1] += v*t/1000
        print(r[1])
    elif opcode == 0x22:
        v = float(ser.readline().rstrip())
        t = float(ser.readline().rstrip())
        r[2] += v*t/1000
        print(r[2])
    elif opcode == 0x30:
        print("T")
        print(ser.readline())

while True:
    try:
        data = ser.readline()
        opcode = int(data.rstrip())
        recv(ser, opcode,r)
    except Exception as e:
        print(e)

    
    """if data.decode().strip() == "d":
        keyboard.press("d")

    if data.decode().strip() == "!d":
        keyboard.release("d")

    if data.decode().strip() == "a":
        keyboard.press("a")

    if data.decode().strip() == "!a":
        keyboard.release("a")

    if data.decode().strip() == "f":
        keyboard.press("f")

    if data.decode().strip() == "!f":
        keyboard.release("f")"""