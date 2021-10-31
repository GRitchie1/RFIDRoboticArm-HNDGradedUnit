from machine import Pin,PWM
import utime
import math


MIN = 500000
MAX = 2500000
MID = math.floor(MIN+((MAX-MIN)/2))

led = Pin(25,Pin.OUT)

class Servo():
    def __init__(self, start_angle = 50, pin_num = 0, minimum = MIN, maximum = MAX):
        self.start_angle = start_angle
        self.maximum = maximum
        self.minimum = minimum
        self.angle = start_angle
        

        #Init Pin
        self.pin = PWM(Pin(pin_num))
        self.pin.freq(50)
        self.pin.duty_ns(self.calc_angle(start_angle))

    def move(self, target_angle):
        self.angle = target_angle
        self.pin.duty_ns(self.calc_angle(target_angle))

    def calc_angle(self, num):
        return math.floor(MIN+(((MAX - MIN) * num) / 100)) 

    def move_smoothly(self, target_angle, delay_ms):
        #self.previous_angle = self.angle
        while self.angle < target_angle:
            self.angle +=1
            self.pin.duty_ns(self.calc_angle(self.angle))
            utime.sleep_ms(delay_ms)

        while self.angle > target_angle:
            self.angle -= 1
            self.pin.duty_ns(self.calc_angle(self.angle))
            utime.sleep_ms(delay_ms)


def main():
    print("loop")
    #Rotate base
    base.move_smoothly(100,10)
    utime.sleep(1)

    #Move down
    third.move_smoothly(75, 10)
    second.move_smoothly(0, 10)
    first.move_smoothly(0, 10)
    utime.sleep(1)

    #Move up
    second.move_smoothly(15, 10)
    first.move_smoothly(15, 10)
    third.move_smoothly(25, 10)
    utime.sleep(1)

    #Rotate
    base.move_smoothly(0,10)
    utime.sleep(1)

    #Move down
    third.move_smoothly(75, 10)
    second.move_smoothly(0, 10)
    first.move_smoothly(0, 10)
    utime.sleep(1)

    #Move up
    second.move_smoothly(15, 10)
    first.move_smoothly(15, 10)
    third.move_smoothly(25, 10)
    utime.sleep(1)


#Init Servos
grip = Servo(50,20,1000000,1500000)
third = Servo(50,19,MIN,MAX)
second = Servo(20,18,MIN,MAX)
first = Servo(20,17,MIN,MAX)
base = Servo(100,16,MIN,MAX)

while True:
    main()



