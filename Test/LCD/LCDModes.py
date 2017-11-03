"""This is the diffirent messages for different senarios for the LCD screen"""

import Adafruit_CharLCD as LCD



LCD = LCD.Adafruit_CharLCDPlate()


def standard_mode():
    """This is the standard mode for the LCD screen.
    It displays the price and Status of the machine."""

    LCD.clear()
    LCD.message("Pris:10kr\n")
    LCD.message("Klar")


def payment_mode():
    "This is the state of the LCD screen when payment is being processed."
    LCD.clear()
    LCD.message("Payment is/nBeing processed")


def payment_insufficient():
    "This state is when the payment unable to go through."
    LCD.clear()
    LCD.message("Card not approved")

def display_balance(balance):
    "Display current balance after purchase."
    LCD.clear()
    LCD.message(balance)
