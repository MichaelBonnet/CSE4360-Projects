#!/usr/bin/env pybricks-micropython

###############
### IMPORTS ###
###############

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import print, wait
from pybricks.parameters import Stop

from a_star import *

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize DriveBase variables and the DriveBase
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = wheel_diameter
axle_track     = axle_track

# defining TURN and MOVE variables
MOVE_SPEED = total_degrees_per_foot
MOVE_TIME  = 1350

TURN_SPEED = MOVE_SPEED/2
TURN_TIME  = 875

#########################
### CONTROL FUNCTIONS ###
#########################

def turn_right():
    left_motor.run_time(  -TURN_SPEED, TURN_TIME, Stop.HOLD, False)
    right_motor.run_time(  TURN_SPEED, TURN_TIME, Stop.HOLD, True)

def turn_left():
    left_motor.run_time(   TURN_SPEED, TURN_TIME, Stop.HOLD, False)
    right_motor.run_time( -TURN_SPEED, TURN_TIME, Stop.HOLD, True)

def move_forward():
    left_motor.run_time(   MOVE_SPEED, MOVE_TIME, Stop.HOLD, False)
    right_motor.run_time(  MOVE_SPEED, MOVE_TIME, Stop.HOLD, True)

def move_backward():
    left_motor.run_time(  -MOVE_SPEED, MOVE_TIME, Stop.HOLD, False)
    right_motor.run_time( -MOVE_SPEED, MOVE_TIME, Stop.HOLD, True)

##########################
### PATH ACTUALIZATION ###
##########################

ev3.speaker.beep(1000)

# Instructions:
# 1 = go forward
# 2 = go backward
# 3 = turn left
# 4 = turn right

# Using run_time
for instruction in instructions:
    if   instruction == 1:
        move_forward()
    elif instruction == 2:
        move_backward()
    elif instruction == 3:
        turn_left()
    elif instruction == 4:
        turn_right()

ev3.speaker.beep(1000)
