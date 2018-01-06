import RPi.GPIO as GPIO
import time


def InitIrSensor():
    
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def ReadIrSensor():
##    input_state = GPIO.input(16)
##    if input_state == False:
##        print('1')
##        time.sleep(0.2)
##        return 1
    return GPIO.input(16)

#InitIrSensor()
#while(True):
#    print GPIO.input(16)
#    time.sleep(0.2)

