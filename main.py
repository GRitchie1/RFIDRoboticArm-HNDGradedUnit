from machine import Pin,PWM
import utime
import math
from servo import Servo, MIN, MAX

MID = math.floor(MIN+((MAX-MIN)/2))

led = Pin(25,Pin.OUT)

def main():
    print("loop")
    #Rotate base
    base.move_smoothly(100,10)
    utime.sleep(1)

    #Move down
    third.move_smoothly(75, 10)
    second.move_smoothly(10, 10)
    first.move_smoothly(0, 10)
    grip.move_smoothly(100, 10)
    utime.sleep(1)

    #Move up
    second.move_smoothly(15, 10)
    first.move_smoothly(15, 10)
    third.move_smoothly(25, 10)
    grip.move_smoothly(0, 10)
    utime.sleep(1)

    #Rotate
    base.move_smoothly(0,10)
    utime.sleep(1)

    #Move down
    third.move_smoothly(75, 10)
    second.move_smoothly(10, 10)
    first.move_smoothly(0, 10)
    grip.move_smoothly(100, 10)
    utime.sleep(1)

    #Move up
    second.move_smoothly(15, 10)
    first.move_smoothly(15, 10)
    third.move_smoothly(25, 10)
    grip.move_smoothly(0, 10)
    utime.sleep(1)


#Init Servos
grip = Servo(50,20,1000000,1500000)
third = Servo(50,19,MIN,MAX)
second = Servo(20,18,MIN,MAX)
first = Servo(20,17,MIN,MAX)
base = Servo(100,16,MIN,MAX)

while True:
    main()



