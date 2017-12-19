import RPi.GPIO as GPIO
import time
global end
end = 0


def my_callback(channel):
    print 'snut'
    global end
    end = 1
    alarm()


def alarm():
    while(True):
        time.sleep(0.2)
        print 'ALARMAFAN'
        
def InitTilt():
    #GPIO.setmode(GPIO.BOARD)

    GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback, bouncetime=300)
    print 'dricka'

InitTilt()


##while(end!=1):
##    time.sleep(0.2)
##    print 'Jag heter hendrick'
##    print end
##

