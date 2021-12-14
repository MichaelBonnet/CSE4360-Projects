###############
### IMPORTS ###
###############

from time import time

# We made these functions and data sets for the purpose of making 
# synthetic "sensor readings" from an infrared seeker in lieu
# of getting actual IR readings as we attempted to get it working.

#################
### FUNCTIONS ###
#################

# Defines an "epoch" of time with a certain heading
# for us to test dynamic position changes for signals.
def get_epoch(start_time, heading_list, pace):
    elapsed_time = round( (time() - start_time), 0 )
    allowed_time = pace * len(heading_list)
    # print(elapsed_time)

    if elapsed_time < allowed_time:
        epoch = int( elapsed_time / pace )
        return heading_list[epoch]
    else:
        return heading_list[-1]

######################
### SYNTHETIC DATA ###
######################

# Synthetic IR source direction data
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

# "Fear" behavior call using synthetic data
# braitenburg_fear( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )

# "Aggression" behavior call using synthetic data
# braitenburg_aggression( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )

# "Love" behavior call using synthetic data
# braitenburg_love( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 1) )

# "Explore" behavior call using synthetic data
# braitenburg_explore( tank_pair, get_speed_modifier(us.value()), get_epoch(start_time, turn_towards_from_left, 2) )