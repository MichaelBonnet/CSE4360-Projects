#!/usr/bin/env pybricks-micropython

###############
### IMPORTS ###
###############

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

from a_star import *

#######################
### INITIALIZATIONS ###
#######################

# Initialize the EV3 brick.
ev3 = EV3Brick()

# Initialize DriveBase variables and the DriveBase
left_motor  = Motor(Port.B)
right_motor = Motor(Port.C)

wheel_diameter = 69
axle_track     = 102

robot = DriveBase(left_motor, right_motor, wheel_diameter, axle_track)

# Defining adjusted degrees for turns
right_90 =  118
left_90  = -118

###################
### PATHFINDING ###
###################

start         = start_location
goal          = goal_location
robot_heading = initial_heading

workspace = generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations)
came_from, cost_so_far = a_star_search(workspace, start, goal)

found_path       = reconstruct_path(came_from, start=start, goal=goal)
step_transitions = get_step_transitions(found_path)
instructions     = get_instructions(step_transitions)

draw_grid(grid_columns, grid_rows, grid_obstacles, found_path)

##########################
### PATH ACTUALIZATION ###
##########################

# eep for start of program
ev3.speaker.beep(300, 0.1)
wait(300)
ev3.speaker.beep(300, 0.1)
wait(300)
ev3.speaker.beep(300, 0.1)
wait(300)
ev3.speaker.beep(600, 0.1)
wait(300)

# Instructions:
# 1 = go forward
# 2 = go backward
# 3 = turn left
# 4 = turn right
for instruction in instructions:
    if   instruction == 1:
        robot.straight(305)
    elif instruction == 2:
        robot.straight(-305)
    elif instruction == 3:
        robot.turn(left_90)
        ev3.speaker.beep(500)
        ev3.speaker.beep(500)
    elif instruction == 4:
        robot.turn(right_90)
        ev3.speaker.beep(750)
        ev3.speaker.beep(750)

ev3.speaker.beep(1000)
# robot.turn(90)
# robot.turn(-90)
# robot.turn(90)

