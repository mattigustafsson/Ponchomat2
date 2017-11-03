import time

import Adafruit_CharLCD as LCD

lcd = LCD.Adafruit_CharLCDPlate()


def standardMode():
    "This is the standard mode for the LCD screen. It displays the price and Status of the machine"
    lcd.clear()
    lcd.message("Pris:10kr\n")
    lcd.message("Klar")

def paymentMode():
    "This is the state of the LCD screen when payment is being processed"
    lcd.clear()
    lcd.message("Payment is/nBeing processed")

    