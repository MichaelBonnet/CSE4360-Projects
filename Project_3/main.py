#!/usr/bin/env python3

###############
### IMPORTS ###
###############

# import pybricks
from ev3dev2.sensor import Sensor
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank, MoveSteering
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4, Sensor
from ev3dev2.sensor.lego import UltrasonicSensor
# from ev3dev2.sensor import HiTechnicIRSeeker
from ev3dev2.led import Leds

steer_pair = MoveSteering(OUTPUT_A, OUTPUT_B)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_B)

# left_motor  = LargeMotor(OUTPUT_A)
# right_motor = LargeMotor(OUTPUT_B)
us = UltrasonicSensor(INPUT_1)
# ir = Sensor(INPUT_2, driver_name='ht-nxt-ir-seeker')
# ir.mode = 'DC'
us.MODE_US_DIST_CM = 'US_DIST_CM'


def get_speed_modifier(dist):
    if  dist in range(2400, 2551):
        return 12
    elif dist in range(2200, 2400):
        return 11
    elif dist in range(2000, 2200):
        return 10
    elif dist in range(1800, 2000):
        return 9
    elif dist in range(1600, 1800):
        return 8
    elif dist in range(1400, 1600):
        return 7
    elif dist in range(1200, 1400):
        return 6
    elif dist in range(1000, 1200):
        return 5
    elif dist in range(600, 800):
        return 4
    elif dist in range(400, 600):
        return 3
    elif dist in range(200, 400):
        return 2
    elif dist in range(0, 200):
        return 1

def get_speed_proportion(dist):
    if dist < 100:
        return 0
    else:
        return ( (dist-100) / (2551-100) )

# Accelerates nearer to light
# Turns away from light and stops
def braitenburg_fear(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0:
        tank_pair.off()
    elif ir_direction in range(1, 6):  # 1-5
        tank_pair.on_for_rotations(left_speed=(75 * (1/speed_modifier)), right_speed=(50 * (1/speed_modifier)), rotations=10)
    elif ir_direction in range(6, 10): # 5-9
        tank_pair.on_for_rotations(left_speed=(50 * (1/speed_modifier)), right_speed=(75 * (1/speed_modifier)), rotations=10)


# Accelerates nearer to light
# Turns towards light
def braitenburg_aggression(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 5:
        tank_pair.on(left_speed=(50 * (1/speed_modifier)), right_speed=(50 * (1/speed_modifier)))
    elif ir_direction == 0:
        tank_pair.on_for_rotations(left_speed=(75 * (1/speed_modifier)), right_speed=(50 * (1/speed_modifier)), rotations=10)
    elif ir_direction in range(1, 5):  # 1-4
        tank_pair.on_for_rotations(left_speed=(75 * (1/speed_modifier)), right_speed=(50 * (1/speed_modifier)), rotations=10)
    elif ir_direction in range(6, 10): # 6-9
        tank_pair.on_for_rotations(left_speed=(50 * (1/speed_modifier)), right_speed=(75 * (1/speed_modifier)), rotations=10)

# Decelerates nearer to light
# Turns towards light
def braitenburg_love(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 5:
        tank_pair.on(left_speed=(50 * (speed_modifier / 12)), right_speed=(50 * (speed_modifier / 12)))
    elif ir_direction == 0:
        tank_pair.on_for_rotations(left_speed=(75 * (speed_modifier / 12)), right_speed=(50 * (speed_modifier / 12)), rotations=10)
    elif ir_direction in range(1, 5):  # 1-4
        tank_pair.on_for_rotations(left_speed=(75 * (speed_modifier / 12)), right_speed=(50 * (speed_modifier / 12)), rotations=10)
    elif ir_direction in range(6, 10): # 6-9
        tank_pair.on_for_rotations(left_speed=(50 * (speed_modifier / 12)), right_speed=(75 * (speed_modifier / 12)), rotations=10)

# Decelerates nearer to light
# Turns away from light and stops
def braitenburg_explore(tank_pair, speed_modifier, ir_direction):
    if ir_direction == 0:
        tank_pair.off()
    elif ir_direction in range(1, 6):  # 1-5
        tank_pair.on_for_rotations(left_speed=(75 * (speed_modifier / 12)), right_speed=(50 * (speed_modifier / 12)), rotations=10)
    elif ir_direction in range(6, 10): # 5-9
        tank_pair.on_for_rotations(left_speed=(50 * (speed_modifier / 12)), right_speed=(75 * (speed_modifier / 12)), rotations=10)

while True:
    # decelerate_towards( tank_pair, get_speed_modifier(us.value()) )
    # accelerate_towards( tank_pair, get_speed_modifier(us.value()) )
    # decelerate_towards( tank_pair, get_speed_proportion(us.value()) )
    # accelerate_towards( tank_pair, get_speed_proportion(us.value()) )
    # turn_towards(tank_pair, ir.value() )
    # turn_away(tank_pair, ir.value() ):
    # print( get_speed_proportion(us.value()) )
    # print(ir.value(0))

    # UNCOMMENT
    # ONE
    # BEHAVIOR
    # PER
    # BRAITENBUG

    # Accelerates nearer to light
    # Turns away from light and stops
    braitenburg_fear( tank_pair, get_speed_modifier(us.value()), ir.value() )

    # Accelerates nearer to light
    # Turns towards light
    braitenburg_aggression( tank_pair, get_speed_modifier(us.value()), ir.value() )

    # Decelerates nearer to light
    # Turns towards light
    braitenburg_love( tank_pair, get_speed_modifier(us.value()), ir.value() )

    # Decelerates nearer to light
    # Turns away from light and stops
    braitenburg_explore( tank_pair, get_speed_modifier(us.value()), ir.value() )
