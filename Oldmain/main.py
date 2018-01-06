import RPi.GPIO as GPIO
import time
#import MFRC522
#import signal

##import start
##from start import *
##from start import InitTilt
##from start import my_callback
##from start import alarm
from Write import setMoney
from Write import ScanRFID

import Write
import LCDModes as lcd
import activateEngine as engine
import IrSensor
"""
Globals and constants
"""
global ScanForCard
ScanForCard = Write.continue_reading
"""
initiate all sensors

Tilt
LCD
RFID modul
Distancesensor
"""
IrSensor.InitIrSensor()
"""
Small functions that do not need to be 
in an external class or method

Tilt func
"""
"""
Main flow chart
"""

global end
end = 0

global summa
summa = 0


def my_callback():
    lcd.tiltSensorActivated()
    lcd.flashLCD()

    while True:
        lcd.scanButtons()
        if lcd.scanButtons() is 1:
            #Break to main loop
            mainLoop()

    print 'snut'
    global end
    end = 1


def InitTilt():
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(
        18, GPIO.FALLING, callback=my_callback, bouncetime=300)
    print 'dricka'


#GPIO.setmode(GPIO.BOARD)
##InitIrSensor()

#signal.signal(signal.SIGINT, end_read)
#MIFAREReader = MFRC522.MFRC522()

##standard_mode()
InitTilt()


#
##InitTilt()
##LCD = LCD.Adafruit_CharLCDPlate()
def mainLoop():

    lcd.standard_mode()
    while Write.continue_reading:
        (balance, succsessfulPayment) = ScanRFID()
        if succsessfulPayment is True:
            lcd.payment_mode()
            time.sleep(1)

            #setMoney(Write.MIFAREReader.getSumma()-20)
            #print (Write.MIFAREReader.getSumma()-20)
            lcd.display_balance(balance)

            engine.Rotate_Enginge(0.75)

            #if IrSensor.ReadIrSensor() is 1:

        elif succsessfulPayment is None:
            lcd.payment_insufficient()
            time.sleep(1)
            Write.continue_reading = True

        button = lcd.scanButtons()
        #if button is lcd.SELECT:
        #Add more money to payment card

    if end == 1:
        t_end = time.time() + 5
        #lcd.

        while time.time() < t_end:
            print 'sno inte'


#except KeyboardInterrupt:
#   pass