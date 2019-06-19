"""
Writes digital output to D5 when the button A is held down

Works with the modules:
- Relay
- LED
- Buzzer
"""

from gamebuino_meta import waitForUpdate, display, buttons
import board
import digitalio

myLED = digitalio.DigitalInOut(board.D5)
myLED.direction = digitalio.Direction.OUTPUT

while True:
    waitForUpdate()
    display.clear()
    
    display.print("DIGITAL OUTPUT\nD5: ")
    
    if buttons.repeat(buttons.A, 0):
        myLED.value = True
        display.print("ON")
    else:
        myLED.value = False
        display.print("OFF")
        
    display.print("\n\n'A' TO TURN ON/OFF")