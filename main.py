from machine import Pin,PWM
import utime
import math


MIN = 1000000
MAX = 2000000
MID = math.floor(MIN+((MAX-MIN)/2))

led = Pin(25,Pin.OUT)

class Servo():
    def __init__(self, start_angle = 50, pin_num = 0, minimum = MIN, maximum = MAX):
        self.start_angle = start_angle
        self.maximum = maximum
        self.minimum = minimum

        #Init Pin
        self.pin = PWM(Pin(pin_num))
        self.pin.freq(50)
        self.pin.duty_ns(self.calc_angle(start_angle))

    def move(self, target_angle):
        self.pin.duty_ns(self.calc_angle(target_angle))

    def calc_angle(self, num):
        return math.floor(MIN+(((MAX - MIN) * num) / 100))  

def main():
    print("loop")
    grip.move(100)
    utime.sleep(1)
    grip.move(0)
    utime.sleep(1)


#Init Servos
grip = Servo(50,20,MIN,MAX)

while True:
    main()



