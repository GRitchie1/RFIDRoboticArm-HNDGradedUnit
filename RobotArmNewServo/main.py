from machine import Pin, PWM
from time import sleep

MIN = 1000
MID = 4600
MAX = 9000

grip = PWM(Pin(20))
third = PWM(Pin(19))
second = PWM(Pin(18))
first = PWM(Pin(17))
base = PWM(Pin(16))

grip.freq(50)
third.freq(50)
second.freq(50)
first.freq(50)
base.freq(50)

sleep(1)
third.duty_u16(MIN)
sleep(5)
third.duty_u16(MID)
sleep(5)
third.duty_u16(MAX)
sleep(5)
 
print("done")
