import RPi.GPIO as GPIO
import time
from LCDModes import *
from Write import setMoney
from Write import ScanRFID
from activateEngine import Rotate_Enginge
import Write
import activateEngine
import measure_distance
import Emailconfig as email
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

mcp = Adafruit_MCP230XX(0x20, 16)

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
    GPIO.add_event_detect(
        18, GPIO.FALLING, callback=my_callback, bouncetime=300)
    print 'dricka'


InitTilt()

try:
    while True:
        onOff = 1
        dist = measure_distance.read_distance()
        if dist > 100:
            display_emptyInventory()
        while (dist > 100):
            dist = measure_distance.read_distance()
            time.sleep(0.2)
        standard_mode()
        if dist < 100:  #<-- Ponchos slut
            while (end != 1 and Write.continue_reading):
                print Write.continue_reading
                if ScanRFID() is True:
                    print Write.continue_reading
                    time.sleep(1)
                    if (Write.MIFAREReader.getSumma() > 20):
                        payment_mode()
                        #setMoney(Write.MIFAREReader.getSumma()-20)
                        #print (Write.MIFAREReader.getSumma()-20)
                        display_balance(
                            str(Write.MIFAREReader.getSumma() - 20))
                        Rotate_Enginge()
                        GPIO.setmode(GPIO.BCM)
                        if (GPIO.input(23) == 1):
                            Rotate_Enginge()
                            if (GPIO.input(23) == 1):
                                write_text('Poncho is stuck')
                                while (GPIO.input(23) == 1):
                                    time.sleep(0.2)
                        else:
                            write_text('Pick up poncho')
                            status = GPIO.input(23)
                            while status == 0:
                                time.sleep(0.2)
                                print "test"
                                status = GPIO.input(23)

                            if GPIO.input(23) == 1:
                                dist = measure_distance.read_distance()
                                if dist > 100:  #<-- Ponchos slut
                                    display_emptyInventory()
                                    while (dist > 100):
                                        dist = measure_distance.read_distance()
                                        time.sleep(0.2)
                                    #email.send_mail()
                                #else:
                        standard_mode()
                        Write.continue_reading = True
                    else:
                        payment_insufficient()

                elif scanButtons() == SELECT:
                    check = 0
                    write_text("Put RFID tag\nto scanner")
                    while check == 0:
                        time.sleep(0.2)
                        if (ScanRFID(1, 500) == True):
                            check = 1
                            Write.continue_reading = True
                            write_text("Remove tag")
                            time.sleep(5)
                            write_text(str(Write.MIFAREReader.getSumma()))
                            time.sleep(2)
                            standard_mode()

            if (end == 1):
                t_end = time.time() + 5
                write_text('ta inte min\n ponchomat pls')
                while time.time() < t_end:
                    print 'sno inte'
                    time.sleep(1)
                end = 0

except KeyboardInterrupt:
    GPIO.cleanup()
    pass
