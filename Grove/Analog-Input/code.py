"""
Single player pong game controlled by the analog input A1
"""

from gamebuino_meta import waitForUpdate, display, buttons
import random
import board
from analogio import AnalogIn

# creates myPotentiometer that we will use to read analog input from A1
myPotentiometer = AnalogIn(board.A1)

while True:
    waitForUpdate()
    display.clear()
    
    # update your value from your potentiometer
    myValue = myPotentiometer.value
    
    # print it on screen
    display.print("ANALOG INPUT\nA1: ")
    display.print(myValue)
    
    # maps the value from 0..65536 to 0..64
    myValue = myValue * 64 // 65536
    
    # draw it as a rectangle
    display.drawRect(0, 16, 64, 5)
    display.fillRect(0, 16, myValue, 5)