import time
from machine import I2C, Pin, SPI #import I2C,Pin,SPI library
from mfrc522 import MFRC522 #import RFID reader library

sck = Pin(6, Pin.OUT)    #set RFID sck to GP6
mosi = Pin(7, Pin.OUT)   #set RFID mosi to GP7
miso = Pin(4, Pin.OUT)   #set RFID miso to GP4 
sda = Pin(5, Pin.OUT)    #set RFID sda to GP5 
rst = Pin(8, Pin.OUT)   #set RFID rst to GP18
spi = SPI(0, baudrate=100000, polarity=0, phase=0, sck=sck, mosi=mosi, miso=miso) #initial SPI 
card1 = "0xe58a6223" #change this value to match your testing RFID card 1
card2 = "0xf765bd60" #change this value to match your testing RFID card 2

while True:
    rdr = MFRC522(spi, sda, rst) #initialize reader
    (stat, tag_type) = rdr.request(rdr.REQIDL) #read card ud
    if stat == rdr.OK:
        (stat, raw_uid) = rdr.anticoll()
        if stat == rdr.OK:
            uid = ("0x%02x%02x%02x%02x" % (raw_uid[0], raw_uid[1], raw_uid[2], raw_uid[3]))
            print(uid)
            if uid == card1: #if ID matches card 1, print card 1 detected
                print("card 1 detected!")
                time.sleep(1)
            elif uid == card2:
                print("card 2 detected!")  #if ID matches card 2, print card 2 detected
                time.sleep(1)
            else:  #if ID doesn't match any card, print invalid card
                print("invalid card!")
                time.sleep(1)