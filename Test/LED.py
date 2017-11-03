import RPi.GPIO as GPIO
import time

PIN11 = 11

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN11,GPIO.OUT)

for x in range(0,50):
    GPIO.output(PIN11,  True)
    time.sleep(0.02)
    GPIO.output(PIN11, False)
    time.sleep(0.02)

GPIO.cleanup()