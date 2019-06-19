"""
Reads analog inputs from A1 and A2 and shows them on screen

Works with the modules :
- 2 x Potentiometers
- 1 x Joystick
"""

from gamebuino_meta import waitForUpdate, display
import board
from analogio import AnalogIn

xAxis = AnalogIn(board.A1)
yAxis = AnalogIn(board.A2)

while True:
    waitForUpdate()
    display.clear()
    
    # reads and maps the value from 0..65536 to -range/2..range/2
    range = 40
    x = xAxis.value * range // 65536 - (range // 2)
    y = yAxis.value * range // 65536 - (range // 2)
    
    # print values
    display.print("JOYSTICK")
    display.print("\nA1 x: ")
    display.print(x)
    display.print("\nA2 y: ")
    display.print(y)
    
    # draw the graphic
    offset = 20 # vertical offset
    display.drawRect(0, 0 + offset, range, range)
    display.fillRect(0, x + range // 2 + offset, range, 1)
    display.fillRect(y + range // 2, 0 + offset, 1, range)
    