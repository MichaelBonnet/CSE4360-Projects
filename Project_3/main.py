#!/usr/bin/env python3

###############
### IMPORTS ###
###############

from ev3dev2.sensor import Sensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, Sensor
from ev3dev2.sensor.lego import UltrasonicSensor
from time import time, sleep
from smbus import SMBus
from sys import stderr

#############################
### SENSOR/ACTUATOR SETUP ###
#############################

# Steering setup
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)

# Ultrasonic sensor setup
us = UltrasonicSensor(INPUT_1)
us.MODE_US_DIST_CM = 'US_DIST_CM'

# Infrared Seeker setup
# Open i2c bus 4 (use port # + 2 -- seeker is plugged into port 2)
bus = SMBus(4)


########################
### GLOBAL VARIABLES ###
########################

start_time = time()

########################
### HELPER FUNCTIONS ###
########################

# Takes the distance reading from the ultrasonic sensor,
# which informs the acceleration of the robot
# by converting it to a value that is used as
# a multiplier numerator or denominator,
# depending on desired behavior.
def get_speed_modifier(dist):
    if  dist in range(2000, 2551):
        return 10
    elif dist in range(1750, 2000):
        return 9
    elif dist in range(1500, 1750):
        return 8
    elif dist in range(1250, 1500):
        return 7
    elif dist in range(1000, 1250):
        return 6
    elif dist in range(750, 1000):
        return 5
    elif dist in range(500, 750):
        return 4
    elif dist in range(250, 500):
        return 3
    elif dist in range(100, 250):
        return 2
    elif dist in range(50, 100):
        return 1
    else:
        return 0

# Takes the distance reading from the ultrasonic sensor,
# which informs the acceleration of the robot
# by converting it to a proportional decimal value 
# used as a multiplier numerator or denominator,
# depending on desired behavior.
#   We're not actually using this,
#       in the interest of things not going wildly out of control
#       and so that we have predictable speed ranges.
def get_speed_proportion(dist):
    if dist < 100:
        return 0
    else:
        return ( (dist-100) / (2551-100) )

# Takes the direction reading (0-9) from the IR seeker
# via direct, raw i2c interactions
# and returns it.
def get_ir_direction(bus):
    direction = bus.read_byte_data( 0x01, 0x42 )
    return direction

#############################
### BRAITENBURG BEHAVIORS ###
#############################

# The "Fear" behavior runs away from signals by:
#   Accelerating nearer to "light"
#   Turning away from "light"
#   Stopping if the "light" is out of view
def braitenburg_fear(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0:              # If IR source is fully outside field of view, the bug can "rest" -> stop
        tank_pair.off()
    elif ir_direction in range(1, 6):  # If IR source is in 1-5 (left through center), turn left down gradient to head away
        tank_pair.on_for_rotations(left_speed=(70 * (1/speed_modifier)), right_speed=(100 * (1/speed_modifier)), rotations=1)
    elif ir_direction in range(6, 10): # If IR source is in 6-9 (right of center),     turn right up gradient to head away
        tank_pair.on_for_rotations(left_speed=(100 * (1/speed_modifier)), right_speed=(70 * (1/speed_modifier)), rotations=1)


# The "Aggression" behavior chases the signal by:
#   Accelerating nearer to "light"
#   Turning towards "light"
def braitenburg_aggression(tank_pair, speed_modifier, ir_direction):
    if ir_direction in range(0, 5):    # If IR source is in 0-4 (behind, & left of center), turn right up gradient to head closer
        tank_pair.on_for_rotations(left_speed=(100 * (1/speed_modifier)), right_speed=(70 * (1/speed_modifier)), rotations=1)
    elif ir_direction == 5:            # If IR source is in 5 (center), no more turning necessary, start speeding up on approach
        tank_pair.on(left_speed=(70 * (1/speed_modifier)), right_speed=(70 * (1/speed_modifier)))
    elif ir_direction in range(6, 10): # If IR source is in 6-9 (right of center),          turn left down gradient to head closer
        tank_pair.on_for_rotations(left_speed=(70 * (1/speed_modifier)), right_speed=(100 * (1/speed_modifier)), rotations=1)


# The "Love" behavior approaches the signal coming to rest in front of it by:
#   Decelerating nearer to "light"
#   Turning towards "light"
#   Stopping if the "light" is close enough
def braitenburg_love(tank_pair, speed_modifier, ir_direction):
    if speed_modifier == 0:                # If the signal is close enough, stop to look lovingly into its eyes
        tank_pair.off()
    else:
        if ir_direction in range(0, 5):    # If IR source is in 0-4 (behind, & left of center), turn right up gradient to head closer
            tank_pair.on_for_rotations(left_speed=(100 * (speed_modifier / 10)), right_speed=(70 * (speed_modifier / 10)), rotations=1)
        elif ir_direction == 5:            # If IR source is in 5 (center), no more turning necessary, start slowing down on approach
            tank_pair.on(left_speed=(70 * (speed_modifier / 10)), right_speed=(70 * (speed_modifier / 10)))
        elif ir_direction in range(6, 10): # If IR source is in 6-9 (right of center), turn left down gradient to head closer
            tank_pair.on_for_rotations(left_speed=(70 * (speed_modifier / 10)), right_speed=(100 * (speed_modifier / 10)), rotations=1)


# The "Explore" behavior seeks out new signals by:
#   Decelerating nearer to "light"
#   Turning away from "light"
#   Stopping if there are no new "lights" to see
def braitenburg_explore(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0:              # If IR source is behind: stop moving
        tank_pair.off()
    elif ir_direction in range(1, 6):  # If IR source is in 1-5 (left through center), turn left down gradient to head away
        tank_pair.on_for_rotations(left_speed=(70 * (speed_modifier / 10)), right_speed=(100 * (speed_modifier / 10)), rotations=1)
    elif ir_direction in range(6, 10): # If IR source is in 6-9 (right), turn right up gradient to head away
        tank_pair.on_for_rotations(left_speed=(100 * (speed_modifier / 10)), right_speed=(70 * (speed_modifier / 10)), rotations=1)


##############################
### BEHAVIOR ACTUALIZATION ###
##############################

while True:
    # Sensor Reading Testing
    # print( get_speed_modifier(us.value()) )
    print( get_ir_direction(bus), file=stderr )

    #############################################
    ### UNCOMMENT ONE BEHAVIOR PER BRAITENBUG ###
    ###   PRIOR TO UPLOADING CODE TO AN EV3   ###
    #############################################

    # Braitenburg "Fear" behavior
    #   Accelerates nearer to light
    #   Turns away from light and stops
    # braitenburg_fear( tank_pair, get_speed_modifier(us.value()), get_ir_direction(bus) )

    # Braitenburg "Aggression" behavior
    #   Accelerates nearer to light
    #   Turns towards light
    # braitenburg_aggression( tank_pair, get_speed_modifier(us.value()), get_ir_direction(bus) )

    # Braitenburg "Love" behavior
    #   Decelerates nearer to light
    #   Turns towards light
    # braitenburg_love( tank_pair, get_speed_modifier(us.value()), get_ir_direction(bus) )

    # Braitenburg "Explore" behavior
    #   Decelerates nearer to light
    #   Turns away from light and stops
    # braitenburg_explore( tank_pair, get_speed_modifier(us.value()), get_ir_direction(bus) )
