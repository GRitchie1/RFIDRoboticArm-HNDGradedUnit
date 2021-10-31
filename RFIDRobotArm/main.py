from mfrc522 import MFRC522 #import RFID reader library
from machine import Pin,PWM,I2C, Pin, SPI #import I2C,Pin,SPI library
import utime
import math
from servo import Servo, MIN, MAX

MID = math.floor(MIN+((MAX-MIN)/2))

sck = Pin(6, Pin.OUT)    #set RFID sck to GP6
mosi = Pin(7, Pin.OUT)   #set RFID mosi to GP7
miso = Pin(4, Pin.OUT)   #set RFID miso to GP4 
sda = Pin(5, Pin.OUT)    #set RFID sda to GP5 
rst = Pin(8, Pin.OUT)   #set RFID rst to GP18
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso) #initial SPI 
card1 = "0xd990e0b8" #change this value to match your testing RFID card 1
card2 = "0xf765bd60" #change this value to match your testing RFID card 2



def main():
    rdr = MFRC522(spi, sda, rst) #initialize reader
    (stat, tag_type) = rdr.request(rdr.REQIDL) #read card ud
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1: #if ID matches card 1, print card 1 detected
                print("card 1 detected!")
                third.move_PID(75, 10)
                utime.sleep(1)
                third.move_PID(25, 10)
                utime.sleep(1)
            else:  #if ID doesn't match any card, print invalid card
                print("invalid card!")
                utime.sleep(1)

#Init Servos
grip = Servo(50,20,1000000,1500000)
third = Servo(50,19,MIN,MAX)
second = Servo(20,18,MIN,MAX)
first = Servo(20,17,MIN,MAX)
base = Servo(100,16,MIN,MAX)

while True:
    main()