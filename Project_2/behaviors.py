# maybe for following wall
# (cs.color != 2) | (cs.color != 5) ):

def wall_found():
    if cs.color == 2:
        return True
    else
        return False

def follow_wall():
    while True:
        turn_right_inc(9)
        move_forward_inc(6)

# wander within a "room" by making an ever-expanding clockwise circle
def wander():
    wander_counter = 0

    while not wall_found():
        left_motor.run(200)
        right_motor.run( -50 + wander_counter )
        wander_counter += 1

    if wall_found():
        follow_wall()


def find_goal():
    pass

def clear():
    pass