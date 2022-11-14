#!/usr/bin/env python3
# so that script can be run from Brickman

from ev3dev.dev import *

# Connect infrared and touch sensors to any sensor ports
ir = InfraredSensor() 
ts = TouchSensor()

# Put the infrared sensor into proximity mode.
ir.mode = 'IR-PROX'

while not ts.value():    # Stop program by pressing touch sensor button
    # Infrared sensor in proximity mode will measure distance to the closest
    # object in front of it.
    distance = ir.value()

    if distance < 60:
        Leds.set_color(Leds.LEFT, Leds.RED)
    else:
        Leds.set_color(Leds.LEFT, Leds.GREEN)

Sound.beep()       
Leds.set_color(Leds.LEFT, Leds.GREEN)  
#make sure left led is green before exiting