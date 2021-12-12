def accelerate_towards(tank_pair, speed_modifier):
    tank_pair.on(left_speed=(50 * (1/speed_modifier) ), right_speed=( 50 * (1/speed_modifier) ))
    # with proportion instead of modifier
    # tank_pair.on(left_speed=(50 * (1/speed_modifier) ), right_speed=( 50 * (1/speed_modifier) ))

def decelerate_towards(tank_pair, speed_modifier):
    if speed_modifier >= 1:
        tank_pair.on(left_speed=(50 * (speed_modifier / 12)), right_speed=(50 * (speed_modifier / 12)) )
    else:
        tank_pair.off()

    # with proportion instead of modifier
    # if speed_modifier >= 1:
    #     tank_pair.on(left_speed=(50 * speed_modifier), right_speed=(50 * speed_modifier) )
    # else:
    #     tank_pair.off()

def turn_towards(tank_pair, ir_direction):
    if ir_direction < 5:
        tank_pair.on_for_rotations(left_speed=50, right_speed=75, rotations=10)
    elif ir_direction > 5:
        tank_pair.on_for_rotations(left_speed=75, right_speed=50, rotations=10)
    else:
        tank_pair.on(left_speed=50, right_speed=50)

def turn_away(tank_pair, ir_direction):
    if ir_direction <= 5: # maybe make edge case for 5 where it turns randomly
        tank_pair.on_for_rotations(left_speed=75, right_speed=50, rotations=10)
    elif ir_direction > 5:
        tank_pair.on_for_rotations(left_speed=50, right_speed=75, rotations=10)