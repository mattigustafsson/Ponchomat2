import RPi.GPIO as GPIO
import time
#import MFRC522
#import signal
from LCDModes import *
##import start
##from start import *
##from start import InitTilt
##from start import my_callback
##from start import alarm
from Write import setMoney
from Write import ScanRFID
import Write


global end
end = 0

global summa
summa = 0

def my_callback(channel):
    print 'snut'
    global end
    end = 1


def InitTilt():
    GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, bouncetime=300)
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
try:
    standard_mode()
    while(end!=1 and Write.continue_reading):
        if(ScanRFID()==True):
                payment_mode()
                time.sleep(1)
                print 'starta motorn'
                #setMoney(Write.MIFAREReader.getSumma()-20)
                #print (Write.MIFAREReader.getSumma()-20)
                display_balance(str(Write.MIFAREReader.getSumma()-20))
        elif(ScanRFID == None):
            payment_insufficient()
    if(end == 1):
        t_end = time.time() + 5        
        write_text('ta inte min\n ponchomat pls')
        while time.time() < t_end:
            print 'sno inte'
        
except KeyboardInterrupt:
    pass