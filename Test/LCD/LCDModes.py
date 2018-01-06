"""This is the diffirent messages for different senarios for the LCD screen"""

import time
import Adafruit_CharLCD as lcd

# Char LCD plate button names.
SELECT = 0
RIGHT = 1
DOWN = 2
UP = 3
LEFT = 4

LCD = lcd.Adafruit_CharLCDPlate(address=0x21)

global FLASH
FLASH = 0


def standard_mode():
    """This is the standard mode for the LCD screen.
    It displays the price and Status of the machine."""

    LCD.clear()
    LCD.message("Pris:10kr\n")
    LCD.message("Klar")


def payment_mode():
    """This is the state of the LCD screen when payment is being processed."""
    LCD.clear()
    LCD.message("Payment is\n")
    LCD.message("Being processed")


def payment_insufficient():
    """This state is when the payment unable to go through."""
    LCD.clear()
    LCD.message("Card\n")
    LCD.message("not approved")


def display_balance(balance):
    """Display current balance after purchase."""
    LCD.clear()
    LCD.message("Card balance is:\n")
    LCD.message(balance)


def tiltSensorActivated():
    """
   
    """
    LCD.clear()
    LCD.message("Machine is\nDeactivated")


def flashLCD():
    global FLASH
    if FLASH == 0:
        LCD.set_backlight(FLASH)
        FLASH = 1
    else:
        LCD.set_backlight(FLASH)
        FLASH = 0


def scanButtons():
    if LCD.is_pressed(SELECT):
        return SELECT
    elif LCD.is_pressed(RIGHT):
        return RIGHT


def main():
    "Main function to test the different modes of the LCD Screen."
    standard_mode()
    time.sleep(1)
    payment_mode()
    time.sleep(1)
    payment_insufficient()
    time.sleep(1)
    display_balance("400")
    time.sleep(1)
    tiltSensorActivated()

    while True:
        print scanButtons()
        time.sleep(0.05)

    while True:
        time.sleep(0.2)
        if LCD.is_pressed(SELECT):
            standard_mode()
        elif LCD.is_pressed(RIGHT):
            payment_mode()
        elif LCD.is_pressed(DOWN):
            payment_insufficient()
        elif LCD.is_pressed(UP):
            display_balance("4564")
        elif LCD.is_pressed(LEFT):
            LCD.clear()
            LCD.message("Test")


if __name__ == "__main__":
    main()
