from machine import Pin,PWM
import utime
import math


MIN = 1000000
MAX = 2000000
MID = math.floor(MIN+((MAX-MIN)/2))

led = Pin(25,Pin.OUT)

#Set up pins for Servo control
base_pin = PWM(Pin(16))
base_pin.freq(50)
base_pin.duty_ns(MID)

first_pin = PWM(Pin(17))
first_pin.freq(50)
first_pin.duty_ns(MID)

second_pin = PWM(Pin(18))
second_pin.freq(50)
second_pin.duty_ns(MID)

third_pin = PWM(Pin(19))
third_pin.freq(50)
third_pin.duty_ns(MID)

grip_pin = PWM(Pin(20))
grip_pin.freq(50)
grip_pin.duty_ns(MID)

def calc_angle(num):
    return math.floor(MIN+(((MAX - MIN) * num) / 100))

def move_servos(base=50,first=50,second=50,third=50,grip=50):
    print("move servo")
    base_angle = calc_angle(base)
    first_angle = calc_angle(first)
    second_angle = calc_angle(second)
    third_angle = calc_angle(third)
    grip_angle = calc_angle(grip)

    base_pin.duty_ns(base_angle)
    first_pin.duty_ns(first_angle)
    second_pin.duty_ns(second_angle)
    third_pin.duty_ns(third_angle)
    grip_pin.duty_ns(grip_angle)
    

def main():
    move_servos(grip=0)
    utime.sleep(1)
    move_servos(grip=50)
    utime.sleep(1)
    move_servos(grip=100)
    utime.sleep(1)

while True:
    main()



