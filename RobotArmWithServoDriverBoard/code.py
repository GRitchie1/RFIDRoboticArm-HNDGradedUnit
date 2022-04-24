# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import busio

# Import the PCA9685 module. Available in the bundle and here:
#   https://github.com/adafruit/Adafruit_CircuitPython_PCA9685
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

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

base.angle = 0
first.angle = 140
second.angle = 90
third.angle = 50
gripper.angle = 180

time.sleep(2)

for i in range(0,180):
    base.angle = i
    time.sleep(0.3)
    print(i)

pca.deinit()
