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
from pybricks.ev3devices import Motor, ColorSensor, UltrasonicSensor
from pybricks.parameters import Port, Stop, Color
from pybricks.tools      import wait, StopWatch, DataLog
import math as math
# from ev3dev.ev3 import *

# Imports from other files in directory
# from a_star          import *  # includes specification.py
# from extra_functions import *  # basically just for debug printing

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize DriveBase variables and the DriveBase
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

cs = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S2)

wheel_diameter          = 69
wheel_circumference     = wheel_diameter * math.pi
circumferences_per_foot = 305 / wheel_circumference
total_degrees_per_foot  = (circumferences_per_foot * 360) / 2

turning_speed           = total_degrees_per_foot/2
turning_time            = 750*2
movement_speed          = total_degrees_per_foot
movement_time           = 1175

##########################
### BEHAVIOR FUNCTIONS ###
##########################

def stop_robot():
    left_motor.stop()
    right_motor.stop()
    left_motor.hold()
    right_motor.hold()

def wall_found():
    if cs.color() == Color.BLUE:
        return True
    else:
        return False

def goal_found():
    if us.distance():
        if us.distance() < 330:
            return True
        else:
            return False
    else:
        return False
    # if cs.color == 5:
    #     return True
    # else:
    #     return False

def follow_wall():
    ev3.speaker.say("Entering Wall Following Mode")

    # left_motor.run(-100)
    # right_motor.run(-100)
    # wait(100)

    while goal_found() == False:
        if wall_found():
            left_motor.run(100)
            right_motor.stop()
            wait(50)
            if wall_found():
                while wall_found():
                    right_motor.run(-200)
                right_motor.stop()
        else:
            right_motor.run(100)
            left_motor.stop()
            wait(50)
    
    if goal_found():
        stop_robot()
        ev3.speaker.say("Found The Mother Fucking Goal While In Wall Following Mode")
        clear()

# wander within a "room" by making an ever-expanding clockwise circle
def wander():

    ev3.speaker.say("Entered Wander Mode")

    wander_counter = 0

    while wall_found() == False | goal_found() == False:
        left_motor.run(200)
        right_motor.run(50 + wander_counter )
        wander_counter = wander_counter + .1
        if (wander_counter + 50) == 200:
            left_motor.run(2000)
            right_motor.run(2000)
            wander_counter = 0
        wait(50)

    if wall_found() == True:
        stop_robot()
        follow_wall()

    if goal_found() == True:
        stop_robot()
        ev3.speaker.say("Found The Mother Fucking Goal While In Wander Mode")
        clear()

def find_goal():
    pass

def clear():
    ev3.speaker.say("Entering Kill Mode")

    kill_counter = 0

    # do:
    left_motor.run(200)
    right_motor.run(200)
    wait(200)

    while ( (wall_found() == False) & (kill_counter < 40) ):
        left_motor.run(200)
        right_motor.run(200)
        wait(200)
        kill_counter += 1
        print(kill_counter)

    if kill_counter >= 40:
        ev3.speaker.say("The monster is vanquished!")
    
    if wall_found():
        stop_robot()
        ev3.speaker.say("Found Wall While In Kill Mode")
        print(cs.color())
        follow_wall()

    # wait(1500)

##########################
### PATH ACTUALIZATION ###
##########################

# beep to indicate start of run
ev3.speaker.say("Starting Run Now")

# follow the found path

# wander()
#     when wall found
#         follow_wall()
#     when goal found
#         clear()

wander()

# clear()

# while True:
#     if cs.color() == Color.BLACK:
#         print("BLACK")
#     elif cs.color() == Color.BLUE:
#         print("BLUE")
#     elif cs.color() == Color.GREEN:
#         print("GREEN")
#     elif cs.color() == Color.YELLOW:
#         print("YELLOW")
#     elif cs.color() == Color.RED:
#         print("RED")
#     elif cs.color() == Color.WHITE:
#         print("WHITE")
#     elif cs.color() == Color.BROWN:
#         print("BROWN")
#     else:
#         print("IMPROPER SENSING")

# beep to indicate end of run
# ev3.speaker.say("Run Complete")
