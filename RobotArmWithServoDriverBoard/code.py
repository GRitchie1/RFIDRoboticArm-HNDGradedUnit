import time
import board
import busio
import digitalio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

#Init GPIO
startButton = digitalio.DigitalInOut(board.GP16)
startButton.switch_to_input(pull=digitalio.Pull.UP)

i2c = busio.I2C(board.GP1, board.GP0)

# Create a simple PCA9685 class instance.
pca = PCA9685(i2c)
pca.frequency = 50

# This is an example for the Micro servo - TowerPro SG-92R: https://www.adafruit.com/product/169
base = servo.Servo(pca.channels[0], min_pulse=500, max_pulse=2400)
first = servo.Servo(pca.channels[1], min_pulse=500, max_pulse=2400)
second = servo.Servo(pca.channels[2], min_pulse=500, max_pulse=2400)
third = servo.Servo(pca.channels[3], min_pulse=500, max_pulse=2400)
gripper = servo.Servo(pca.channels[4], min_pulse=500, max_pulse=2400)

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
    for i in range(first.angle, 75, -1):
        first.angle = i
        time.sleep(0.02)
        
    for i in range(second.angle, 70, -1):
        second.angle = i
        time.sleep(0.02)

    #Lift after scanning item
    print("Lift after scanning item")
    for i in range(first.angle, 140, 1):
        first.angle = i
        time.sleep(0.02)
        
    for i in range(second.angle, 90, 1):
        second.angle = i
        time.sleep(0.02)
        
    #Rotate to Output position
    print("Rotate to Output position")
    for i in range(base.angle, 180, 1):      #Add if statement from scanned ID
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
        
while True:
    if not startButton.value:
        print("Move")
        Movement_Cycle()
    time.sleep(0.1)

pca.deinit()
