"""
Reads Digital input from D5 and shows it on screen

Works with the modules:
- Switch
- Tactile switch
"""

from gamebuino_meta import waitForUpdate, display
import board
import digitalio

mySwitch = digitalio.DigitalInOut(board.D5)
mySwitch.direction = digitalio.Direction.INPUT

while True:
    waitForUpdate()
    display.clear()
    
    myValue = mySwitch.value
    
    display.print("DIGITAL INPUT\nD5: ")
    display.print(str(myValue))
    display.print("\n\n")
    
    if myValue:
        display.print("ON")
    else:
        display.print("OFF")