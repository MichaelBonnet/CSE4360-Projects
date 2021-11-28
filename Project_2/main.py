#!/usr/bin/env pybricks-micropython

# Authors : Michael Bonnet
#           Allison Gardiner
#           Noah Walker
# Class   : CSE 4360-001 Autonomous Robots @ UT Arlington
#           Taught by Dr. Manfred Huber in Fall 2021
# Project : Project 1

# Due Date           : 11/3/2021 @ 11:59 PM
# Submission Date    : TBD
# Demonstration Date : 11/3/2021 @ 7:15 PM
# Grade Received     : TBD

###############
### IMPORTS ###
###############

# pybricks imports for the ev3, motors, ports, and Stop
from pybricks.hubs       import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port, Stop
from ev3dev.ev3 import *

# Imports from other files in directory
from a_star          import *  # includes specification.py
from extra_functions import *  # basically just for debug printing

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize DriveBase variables and the DriveBase
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

ts = TouchSensor()

wheel_diameter = 69
wheel_circumference = wheel_diameter * math.pi
circumferences_per_foot = 305 / wheel_circumference
total_degrees_per_foot = (circumferences_per_foot * 360) / 2

# if d_version == 1:
#     turning_speed  = total_degrees_per_foot/2
#     turning_time   = 875
#     movement_speed = total_degrees_per_foot
#     movement_time  = 1350
# elif d_version == 2:

    turning_speed  = total_degrees_per_foot/2
    turning_time   = 750*2
    movement_speed = total_degrees_per_foot
    movement_time  = 1175

#########################
### CONTROL FUNCTIONS ###
#########################

# Turns ev3 in place to the left by 90 degrees
def turn_left():
    left_motor.run_time(  -turning_speed,  turning_time,  Stop.HOLD, False)
    right_motor.run_time(  turning_speed,  turning_time,  Stop.HOLD, True)

# Turns ev3 in place to the right by 90 degrees
def turn_right():
    left_motor.run_time(   turning_speed,  turning_time,  Stop.HOLD, False)
    # right_motor.run_time( -turning_speed,  turning_time,  Stop.HOLD, True)
    right_motor.run_time( -turning_speed-8,  turning_time,  Stop.HOLD, True)

# Moves ev3 forward wrt current heading by either 6 or 12 inches
def move_forward():
    left_motor.run_time(   movement_speed, movement_time, Stop.HOLD, False)
    right_motor.run_time(  movement_speed,    movement_time, Stop.HOLD, True)

# Moves ev3 backward wrt current heading by either 6 or 12 inches
def move_backward():
    left_motor.run_time(  -movement_speed, movement_time, Stop.HOLD, False)
    right_motor.run_time( -movement_speed,    movement_time, Stop.HOLD, True)

##########################
### PATH ACTUALIZATION ###
##########################

# beep to indicate start of run
ev3.speaker.beep(1000)

# follow the found path

# beep to indicate end of run
ev3.speaker.beep(1000)


###########################################
### AUTOMATICALLY GENERATED BOILERPLATE ###
###########################################

#!/usr/bin/env pybricks-micropython
# from pybricks.hubs import EV3Brick
# from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
#                                  InfraredSensor, UltrasonicSensor, GyroSensor)
# from pybricks.parameters import Port, Stop, Direction, Button, Color
# from pybricks.tools import wait, StopWatch, DataLog
# from pybricks.robotics import DriveBase
# from pybricks.media.ev3dev import SoundFile, ImageFile


# # This program requires LEGO EV3 MicroPython v2.0 or higher.
# # Click "Open user guide" on the EV3 extension tab for more information.


# # Create your objects here.
# ev3 = EV3Brick()


# # Write your program here.
# ev3.speaker.beep()
