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
    """
    1 when no thing in between
    0 when a thing is in between
    """
    return GPIO.input(16)


while True:
    print ReadIrSensor()
    time.sleep(0.2)
