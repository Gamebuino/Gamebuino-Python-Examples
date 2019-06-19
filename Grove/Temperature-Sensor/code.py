"""
Reads the temperature from A1 and shows it on screen

Works with the modules :
- Temperature Sensor
"""

from gamebuino_meta import waitForUpdate, display
import board
from analogio import AnalogIn
import math

# creates myPotentiometer that we will use to read analog input from A1
thermistor = AnalogIn(board.A1)

while True:
    waitForUpdate()
    display.clear()

    # reads the value from the thermocouple and convert it to temperature
    temperature = 999.99
    B = 4275.0;  # B value of the thermistor
    R0 = 100000.0;  # R0 = 100k
    R = 65536.0 / thermistor.value - 1.0 # analog input
    R = R0 * R
    if R/R0 > 0 :
        temperature = 1.0 / ( math.log(R / R0) / B + 1 / 298.15 ) - 273.15;

    # print it on screen
    display.print("TEMPERATURE SENSOR\nA1: ")
    display.print(thermistor.value)
    display.print("\nTEMP: ")
    display.print(str(temperature))
    display.print("C")