import time
import board
import busio
import digitalio
import mfrc522
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

#Init GPIO
startButton = digitalio.DigitalInOut(board.GP16)
startButton.switch_to_input(pull=digitalio.Pull.UP)

#Init SPI for RFID
sck = board.GP6
mosi = board.GP7
miso = board.GP4
spi = busio.SPI(sck, MOSI=mosi, MISO=miso)

#Init I2C for motor control
i2c = busio.I2C(board.GP1, board.GP0)

#Init RFID
cs = digitalio.DigitalInOut(board.GP5)
rst = digitalio.DigitalInOut(board.GP8)
rfid = mfrc522.MFRC522(spi, cs, rst)
rfid.set_antenna_gain(0x07 << 4)

# Create Servos
pca = PCA9685(i2c)
pca.frequency = 50

base = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2400)
first = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2400)
second = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2400)
third = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2400)
gripper = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2400)


#Setup
prev_data = None
prev_time = 0
timeout = 1

#Starting position
base.angle = 1
first.angle = 140
second.angle = 90
third.angle = 50
gripper.angle = 180
time.sleep(2)

def Movement_Cycle():
    #Open Gripper
    print("open gripper")
    for i in range(gripper.angle, 120, -1):
        gripper.angle = i
        time.sleep(0.02)

    #Move to pick up item
    print("Move to pick up item")
    for i in range(first.angle, 80, -1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 70, -1):
        second.angle = i
        time.sleep(0.02)

    for i in range(third.angle, 30, -1):
        third.angle = i
        time.sleep(0.02)

    #Close Gripper
    print("Close Gripper")
    for i in range(gripper.angle, 180, 1):
        gripper.angle = i
        time.sleep(0.02)

    #Lift item
    print("Lift item")
    for i in range(first.angle, 140, 1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 90, 1):
        second.angle = i
        time.sleep(0.02)

    for i in range(third.angle, 50, 1):
        third.angle = i
        time.sleep(0.02)

    #Rotate to RFID
    print("Rotate to RFID")
    for i in range(base.angle, 40, 1):
        base.angle = i
        time.sleep(0.02)

    #Move to scan item
    print("Move to scan item")
    for i in range(first.angle, 85, -1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 60, -1):
        second.angle = i
        time.sleep(0.02)

    #Scan Item
    partID = None
    timer = 0
    while timer < 3 and partID == None:
        data = ReadRFID()
        if data:
            partID = data
            print(data)
        timer+= 1
        time.sleep(1)

    if partID:
        print(f"{partID=}")
    else:
        print("No part detected")


    #Lift after scanning item
    print("Lift after scanning item")
    for i in range(first.angle, 140, 1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 90, 1):
        second.angle = i
        time.sleep(0.02)

    #Rotate to Output position

    if partID == "d990e0b8":
        target_output = 90
    else:
        target_output = 180


    print(f"Rotate to Output position {target_output}")
    for i in range(base.angle, target_output, 1):      #Add if statement from scanned ID
        base.angle = i
        time.sleep(0.02)

    #Move to place item
    print("Move to place item")
    for i in range(first.angle, 80, -1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 70, -1):
        second.angle = i
        time.sleep(0.02)

    for i in range(third.angle, 30, -1):
        third.angle = i
        time.sleep(0.02)

    #Open Gripper
    print("Open Gripper")
    for i in range(gripper.angle, 120, -1):
        gripper.angle = i
        time.sleep(0.02)

    #Lift arm
    print("Lift arm")
    for i in range(first.angle, 140, 1):
        first.angle = i
        time.sleep(0.02)

    for i in range(second.angle, 90, 1):
        second.angle = i
        time.sleep(0.02)

    for i in range(third.angle, 50, 1):
        third.angle = i
        time.sleep(0.02)

    #Close Gripper
    print("Close Gripper")
    for i in range(gripper.angle, 180, 1):
        gripper.angle = i
        time.sleep(0.02)

    #Rotate to Starting position
    print("Rotate to Starting position")
    for i in range(base.angle, 1, -1):      #Add if statement from scanned ID
        base.angle = i
        time.sleep(0.02)


def ReadRFID():
    global prev_time
    global prev_data

    (status, tag_type) = rfid.request(rfid.REQALL)
    if status == rfid.OK:
        (status, raw_uid) = rfid.anticoll()

        if status == rfid.OK:
            rfid_data = "{:02x}{:02x}{:02x}{:02x}".format(raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3])

            if rfid_data != prev_data:
                prev_data = rfid_data

                print("Card detected! UID: {}".format(rfid_data))
            prev_time = time.monotonic()
    else:
        if time.monotonic() - prev_time > timeout:
            prev_data = None

    return prev_data


while True:
    if not startButton.value:
        print("Move")
        Movement_Cycle()
    time.sleep(0.1)

pca.deinit()
