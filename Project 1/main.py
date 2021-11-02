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

# imports from other files in folder
from a_star          import *  # includes specification.py
from extra_functions import *

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize DriveBase variables and the DriveBase
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

# defining variables for turning and moving
movement_speed = total_degrees_per_foot
movement_time  = 1350

turning_speed  = movement_speed/2
turning_time   = 875

#########################
### CONTROL FUNCTIONS ###
#########################

def turn_right():
    left_motor.run_time(  -turning_speed,  turning_time,  Stop.HOLD, False)
    right_motor.run_time(  turning_speed,  turning_time,  Stop.HOLD, True)

def turn_left():
    left_motor.run_time(   turning_speed,  turning_time,  Stop.HOLD, False)
    right_motor.run_time( -turning_speed,  turning_time,  Stop.HOLD, True)

def move_forward():
    left_motor.run_time(   movement_speed, movement_time, Stop.HOLD, False)
    right_motor.run_time(  movement_speed, movement_time, Stop.HOLD, True)

def move_backward():
    left_motor.run_time(  -movement_speed, movement_time, Stop.HOLD, False)
    right_motor.run_time( -movement_speed, movement_time, Stop.HOLD, True)

def execute_path(instructions):
    for instruction in instructions:
        if   instruction == 1:
            move_forward()
        elif instruction == 2:
            move_backward()
        elif instruction == 3:
            turn_left()
        elif instruction == 4:
            turn_right()

##########################
### PATH ACTUALIZATION ###
##########################

# beep to indicate start of run
ev3.speaker.beep(1000)

# follow the found path
execute_path(instructions)

# beep to indicate end of run
ev3.speaker.beep(1000)
