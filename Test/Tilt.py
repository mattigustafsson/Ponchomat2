import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.IN)

try:
    while 1:
        if GPIO.input(11):
            print ("Jag lutar!!")
            time.sleep(0.5)
        else:
            print ("Jag lutar inte.")
            time.sleep(0.5)
finally:
    GPIO.cleanup()    

