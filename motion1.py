#!/usr/bin/env python3
from ev3dev.ev3 import *
import os
os.system('setfont Lat15-TerminusBold14')
mL = LargeMotor('outB'); mL.stop_action = 'hold'
mR = LargeMotor('outC'); mR.stop_action = 'hold'
print('Hello, my name is EV3!')
Sound.speak('Hello, my name is EV3!').wait()
mL.run_to_rel_pos(position_sp= 4000, speed_sp = 500)
mR.run_to_rel_pos(position_sp= 4000, speed_sp = 500)
mL.wait_while('running')
mR.wait_while('running')