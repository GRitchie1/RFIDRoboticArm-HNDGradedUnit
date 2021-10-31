from machine import Pin,PWM
import utime
import math

MIN = 500000
MAX = 2500000

class Servo():
    def __init__(self, start_angle = 50, pin_num = 0, minimum = MIN, maximum = MAX):
        self.start_angle = start_angle
        self.maximum = maximum
        self.minimum = minimum
        self.angle = start_angle
        self.error = 0
        self.prev_error = 0
        self.sum_error = 0

        #Init Pin
        self.pin = PWM(Pin(pin_num))
        self.pin.freq(50)
        self.pin.duty_ns(self.calc_angle(start_angle))
        print("init")

    def move(self, target_angle):
        self.angle = target_angle
        self.pin.duty_ns(self.calc_angle(target_angle))

    def calc_angle(self, num):
        return int(math.floor(MIN+(((MAX - MIN) * num) / 100)))

    def move_smoothly(self, target_angle, delay_ms):
        while self.angle < target_angle:
            self.angle +=1
            self.pin.duty_ns(self.calc_angle(self.angle))
            utime.sleep_ms(delay_ms)

        while self.angle > target_angle:
            self.angle -= 1
            self.pin.duty_ns(self.calc_angle(self.angle))
            utime.sleep_ms(delay_ms)
    
    def move_PID(self, target_angle, delay_ms):
        KP = 0.02 #0.02
        KD = 0.01 #0.01
        KI = 0.005 #0.005

        while self.angle != target_angle:
            self.error = target_angle - self.angle
        
            new_angle = self.angle+((self.error * KP) + (self.prev_error * KD) + (self.sum_error * KI))
            new_angle = max(min(100, new_angle), 0)

            self.sum_error += self.error
            self.prev_error = self.error

            self.pin.duty_ns(self.calc_angle(new_angle))
            self.angle=int(math.floor(new_angle))
            utime.sleep_ms(15)
        
        
