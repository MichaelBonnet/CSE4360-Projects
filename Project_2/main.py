#!/usr/bin/env pybricks-micropython

# Authors : Michael Bonnet
#           Allison Gardiner
#           Noah Walker
# Class   : CSE 4360-001 Autonomous Robots @ UT Arlington
#           Taught by Dr. Manfred Huber in Fall 2021
# Project : Project 2

# Due Date           : 11/30/2021 @ 11:59 PM
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
from pybricks.nxtdevices import LightSensor

# Extra functions from other .py file
from extra_functions import *

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize Motors
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

# Initialize Sensors
cs = ColorSensor(Port.S1)
us = UltrasonicSensor(Port.S2)
ls = LightSensor(Port.S3)

# Other stuff
watch = StopWatch()
watch.pause()
watch.reset()

##########################
### BEHAVIOR FUNCTIONS ###
##########################

# Stopping Helper Function
#   Used to help smoothly transition between behaviors in 
#   follow_wall() and wander() and clear()
def stop_robot():
    left_motor.stop()
    right_motor.stop()
    left_motor.hold()
    right_motor.hold()

# Wall Finding Helper Function
#   Used as a continuation condition for the while loops in
#   follow_wall() and wander() and clear()
def wall_found():
    if cs.color() == Color.BLUE:
        return True
    else:
        return False

# Wall Finding Helper Function
#   Used as a continuation condition for the while loops in
#   follow_wall() and wander() and clear()
def wall_found_right():
    if ( (ls.reflection() >= 10) & (ls.reflection() <= 20) ):
        return True
    else:
        return False

# Goal Finding Behavior
#   Used as a continuation condition for the while loops in
#   follow_wall() and wander()
def goal_found():
    if us.distance():
        if us.distance() < 330:
            return True
        else:
            return False
    else:
        return False

# Wall Following Behavior
#   Follows a wall until a goal is detected.
#   Calls wall_found_left() and goal_found() as continuation conditions, and
#         clear() as a behavior change.
def follow_wall():
    ev3.speaker.say("Entering Wall Following Mode")

    watch.resume()

    while (goal_found() == False) & ( watch.time() < (80 * 1000) ):
        print("entered first order while loop")
        if wall_found():
            left_motor.run(200)
            right_motor.stop()
            wait(200)
        if wall_found():
            left_motor.stop()
            while wall_found():
                right_motor.run(-200)
            right_motor.stop()
        else:
            right_motor.run(200)
            left_motor.stop()
            wait(200)

    if watch.time() >= (80 * 1000):
        stop_robot()
        watch.pause()
        watch.reset()
        left_motor.run(100)
        right_motor.run(-100)
        stop_robot()
        wander()


    if goal_found():
        stop_robot()
        ev3.speaker.say("Found Goal While In Wall Following Mode")
        clear()

    # while goal_found() == False:
    #     if wall_found_right():
    #         while wall_found_right():
    #             right_motor.run(-200)
    #             left_motor.stop()
    #             wait(200)
    #     if wall_found_left():
    #         left_motor.run(200)
    #         right_motor.stop()
    #         wait(200)
    #     if wall_found_left():
    #         while wall_found_left():
    #             # left_motor.run(-100) #
    #             right_motor.run(-200)
    #             left_motor.stop()
    #             # right_motor.stop() #
    #             wait(200)
    #     else:
    #         right_motor.run(200)
    #         left_motor.stop()
    #         wait(200)

    # while goal_found() == False:
    #     if wall_found():
    #         while wall_found():
    #             left_motor.run(-100)
    #             right_motor.stop()
    #             wait(100)
    #         right_motor.run(-400)
    #         wait(400)
    #         if wall_found():
    #             while wall_found():
    #                 right_motor.run(-100)
    #             right_motor.stop()
    #     else:
    #         ev3.speaker.say("Moving Forward")
    #         right_motor.run(100)
    #         left_motor_run(100)
    #         right_motor.stop()
    #         left_motor.stop()
    #         wait(100)

    # while goal_found() == False:
    #     if wall_found():
    #         left_motor.run(-60)
    #         right_motor.run(-200)
    #         left_motor.stop()
    #         right_motor.stop()
    #         wait(200)
    #     else:
    #         left_motor.run(100)   # previously
    #         right_motor.run(100) # previously 30, then 100
    #         left_motor.stop()
    #         right_motor.stop()
    #         wait(100)

# Clearing Behavior
#   Only entered when another behavior detects a goal,
#       it charges forward towards the detected goal
#       until it either hits a wall (and enters follow_wall() or 
#       or has charged far enough forward that it has 
#       achieved the goal by moving it out of position.
#   Calls wall_found_left() as a continuation condition, and
#         follow_wall() as a behavior change.
def clear():
    ev3.speaker.say("Entering Clearing Mode")

    kill_counter = 0

    # do:
    left_motor.run(200)
    right_motor.run(200)
    wait(200)

    while ( (wall_found() == False) & (kill_counter < 16) ):
        ev3.speaker.beep()
        left_motor.run(200)
        right_motor.run(200)
        wait(200)
        kill_counter += 1

    if kill_counter >= 16:
        stop_robot()
        ev3.speaker.say("The monster is vanquished!")
    
    if wall_found():
        stop_robot()
        ev3.speaker.say("Found Wall While In Clear Mode")
        follow_wall()

# Wandering Behavior
#   Wander within a "room" by moving in an expanding clockwise spiral
#       until either a goal or wall is found, in which case it enters
#       clear() or follow_wall(), respectively.
#   Calls wall_found_left() and goal_found() as continuation conditions,
#         follow_wall() and clear() as behavior changes, and
#         stop_robot() to aid in behavior change.
def wander():
    ev3.speaker.say("Entering Wander Mode")

    wander_counter = 0

    while wall_found() == False | goal_found() == False:
        left_motor.run(200)
        right_motor.run(50 + wander_counter )
        wander_counter = wander_counter + .1
        if (wander_counter + 50) == 200:
            while wall_found == False:
                left_motor.run(200)
                right_motor.run(200)
                wait(200)
            stop_robot()
            wander_counter = 0
            follow_wall()
        wait(50)

    if wall_found() == True:
        stop_robot()
        follow_wall()

    if goal_found() == True:
        stop_robot()
        ev3.speaker.say("Found Goal While In Wander Mode")
        clear()

##############################
### BEHAVIOR ACTUALIZATION ###
##############################

# Announce run start
ev3.speaker.say("Starting Run Now")

# Start by wandering
wander()

# check_light_sensor(ls)

# Announce run end
ev3.speaker.say("Run Complete")
