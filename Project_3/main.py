#!/usr/bin/env python3

###############
### IMPORTS ###
###############

from ev3dev2.sensor import Sensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, Sensor
from ev3dev2.sensor.lego import UltrasonicSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.port import LegoPort
from time import time, sleep
from smbus import SMBus
from sys import stderr
# import pybricks

#############################
### SENSOR/ACTUATOR SETUP ###
#############################

# Steering setup
steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)

# Ultrasonic sensor setup
us = UltrasonicSensor(INPUT_1)
us.MODE_US_DIST_CM = 'US_DIST_CM'

port = LegoPort(INPUT_2)
port.mode = 'other-i2c'
sleep(2)

ir = Sensor(INPUT_2)

bus = SMBus(4)
address = 0x01

# block = bus.read_i2c_block_data(address, 0, 13)
# print(block)

# bus4 = i2c.SMBus('/dev/i2c-in2') 
# bus4.set_address(0x01)

# Infrared seeker setup
# ir = Sensor(INPUT_2, driver_name='ht-nxt-ir-seek-v2')
# ir = InfraredSensor(INPUT_2)
# ir.mode = 'DC'

########################
### GLOBAL VARIABLES ###
########################

start_time = time()

turn_towards_from_left = [
    2,
    3,
    4,
    5
]

turn_towards_from_right = [
    8,
    7,
    6,
    5
]

turn_away_from_left = [
    3,
    2,
    1,
    0
]

turn_away_from_right = [
    7,
    8,
    9,
    0
]

turn_towards_from_back = [
    0,
    1,
    2,
    3,
    4,
    5
]

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
    # elif dist in range(0, 100):
    #     return 1
    # else:
    #     return 0

# Takes the distance reading from the ultrasonic sensor,
# which informs the acceleration of the robot
# by converting it to a proportional decimal value 
# used as a multiplier numerator or denominator,
# depending on desired behavior.
def get_speed_proportion(dist):
    if dist < 100:
        return 0
    else:
        return ( (dist-100) / (2551-100) )

# Defines an "epoch" for us to test dynamic position changes for signals
# while we continue to find out how to use our IR sensor.
def get_epoch(start_time, heading_list, pace):
    elapsed_time = round( (time() - start_time), 0 )
    allowed_time = pace * len(heading_list)
    # print(elapsed_time)

    if elapsed_time < allowed_time:
        epoch = int( elapsed_time / pace )
        return heading_list[epoch]
    else:
        return heading_list[-1]


#############################
### BRAITENBURG BEHAVIORS ###
#############################

# The "Fear" behavior runs away from signals by:
#   Accelerating nearer to "light"
#   Turning away from "light"
#   Stopping if the "light" is out of view
def braitenburg_fear(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0: # If IR source is fully outside field of view, the bug can "rest" -> stop
        tank_pair.off()
    elif ir_direction in range(1, 6):  # If IR source is in 1-5 (left through center), turn left down gradient to head away
        tank_pair.on_for_rotations(left_speed=(50 * (1/speed_modifier)), right_speed=(75 * (1/speed_modifier)), rotations=1)
    elif ir_direction in range(6, 10): # If IR source is in 6-9 (right of center),     turn right up gradient to head away
        tank_pair.on_for_rotations(left_speed=(75 * (1/speed_modifier)), right_speed=(50 * (1/speed_modifier)), rotations=1)


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
    if speed_modifier == 0: # If the signal is close enough, stop to look lovingly into its eyes
        tank_pair.off()
    else:
        if ir_direction in range(0, 5):    # If IR source is in 0-4 (behind, & left of center), turn right up gradient to head closer
            tank_pair.on_for_rotations(left_speed=(75 * (speed_modifier / 10)), right_speed=(50 * (speed_modifier / 10)), rotations=1)
        elif ir_direction == 5:            # If IR source is in 5 (center), no more turning necessary, start slowing down on approach
            tank_pair.on(left_speed=(50 * (speed_modifier / 10)), right_speed=(50 * (speed_modifier / 10)))
        elif ir_direction in range(6, 10): # If IR source is in 6-9 (right of center), turn left down gradient to head closer
            tank_pair.on_for_rotations(left_speed=(50 * (speed_modifier / 10)), right_speed=(75 * (speed_modifier / 10)), rotations=1)

# The "Explore" behavior seeks out new signals by:
#   Decelerating nearer to "light"
#   Turning away from "light"
#   Stopping if there are no new "lights" to see
def braitenburg_explore(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0:   # If IR source is behind: stop moving
        tank_pair.off()
    elif ir_direction in range(1, 6):  # If IR source is in 1-5 (left through center), turn left down gradient to head away
        tank_pair.on_for_rotations(left_speed=(50 * (speed_modifier / 10)), right_speed=(75 * (speed_modifier / 10)), rotations=1)
    elif ir_direction in range(6, 10): # If IR source is in 6-9 (right), turn right up gradient to head away
        tank_pair.on_for_rotations(left_speed=(75 * (speed_modifier / 10)), right_speed=(50 * (speed_modifier / 10)), rotations=1)

##############################
### BEHAVIOR ACTUALIZATION ###
##############################

while True:
    block = bus.read_i2c_block_data(address, 0, 1)
    print( str(block), file=stderr )
    print ( str(port.device_name) )
    print ( str(port.device_name()) )
    print ( str(port.modes()) )
    # print('Firmware version: {}.{}\n'.format(str(block[8]), str(block[9])), file=stderr)
    #############################################
    ### UNCOMMENT ONE BEHAVIOR PER BRAITENBUG ###
    ###   PRIOR TO UPLOADING CODE TO AN EV3   ###
    #############################################

    #############################################
    ### Also, pick a heading list & pace for  ###
    ### the get_epoch() function if need be   ###
    #############################################

    # Braitenburg "Fear" behavior
    #   Accelerates nearer to light
    #   Turns away from light and stops
    # braitenburg_fear( tank_pair, get_speed_modifier(us.value()), ir.value() ) # Once we actually get the IR seeker working
    # braitenburg_fear( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )          # Until we actually get the IR seeker working

    # Braitenburg "Aggression" behavior
    #   Accelerates nearer to light
    #   Turns towards light
    # braitenburg_aggression( tank_pair, get_speed_modifier(us.value()), ir.value() ) # Once we actually get the IR seeker working
    # braitenburg_aggression( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )          # Until we actually get the IR seeker working

    # Braitenburg "Love" behavior
    #   Decelerates nearer to light
    #   Turns towards light
    # braitenburg_love( tank_pair, get_speed_modifier(us.value()), ir.value() ) # Once we actually get the IR seeker working
    # braitenburg_love( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 1) )          # Until we actually get the IR seeker working

    # Braitenburg "Explore" behavior
    #   Decelerates nearer to light
    #   Turns away from light and stops
    # braitenburg_explore( tank_pair, get_speed_modifier(us.value()), ir.value() ) # Once we actually get the IR seeker working
    # braitenburg_explore( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )          # Until we actually get the IR seeker working
