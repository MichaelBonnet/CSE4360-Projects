###############
### IMPORTS ###
###############

# import math as math

from implementation import *
from specification import *

# generates and returns a workspace divided into 1' x 1' cells with obstacles marked
def generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations):
    workspace         = GridWithWeights(grid_columns, grid_rows)
    workspace.weights = {loc: 5        for loc in possible_locations}
    workspace.weights = {loc: 10000000 for loc in grid_obstacles}

    # return the newly generated workspace
    return workspace


# generates a list of transitions between steps in found_path in terms of the changes in X and Y
# returns a list of lists where the sublists are ordered pairs of [change in x, change in y] for the transition.
def get_step_transitions(found_path):
    step_transitions = []
    # for n steps there are n-1 step transitions, so only iterate that far
    for i in range(len(found_path)-1):
        x_change  = found_path[i+1][0] - found_path[i][0] # get change in X for next transition
        y_change  = found_path[i+1][1] - found_path[i][1] # get change in Y for next transition
        xy_change = [x_change, y_change]  # create temp list where 0th item is X change and the 1st is Y change
        step_transitions.append(xy_change)    # append temp list to the list of all step transitions

    # return the transitions list
    return step_transitions


# generates a list of instructions in the form of one of four integers (see spec in function body)
# that each correspond to one of: move forward, move backward, turn left 90 degrees, turn right 90 degrees.
# returns the generated list of integers.
def get_instructions(step_transitions):
    # Instructions:
    # 1 = go forward
    # 2 = go backward
    # 3 = turn left
    # 4 = turn right
    instructions = []

    # for each transition,
    for i in range(len(step_transitions)):
        # detect if there was a heading change
        if step_transitions[i][0] != step_transitions[i-1][0] and step_transitions[i][1] != step_transitions[i-1][1]:
            # and if so, what kind of heading change
            x_change  = step_transitions[i][0] - step_transitions[i-1][0]
            y_change  = step_transitions[i][1] - step_transitions[i-1][1]

            # Depending on the heading change,
            if y_change == 1:
                instructions.append(4)  # append right turn instruction
                instructions.append(1)  # append go forward instruction
            elif y_change == -1:
                instructions.append(3)  # append left turn  instruction
                instructions.append(1)  # append go forward instruction
            elif x_change == 1:
                instructions.append(3)  # append left turn  instruction
                instructions.append(1)  # append go forward instruction
            elif x_change == -1:
                instructions.append(4)  # append right turn instruction
                instructions.append(1)  # append go forward instruction
        # if no heading change is detected,
        else:
            instructions.append(1) # just go forward on current heading
    
    # return the instruction list, possibly to be amended later
    return instructions

#############################################
### OPTIONAL PRINTING/DEBUGGING FUNCTIONS ###
#############################################

# prints to console each instruction in list of instructions
# does not return anything
def print_instructions(instructions):
    for i in range(len(instructions)):
        if instructions[i] == 1:
            instruction_text = "go    forward"
        elif instructions[i] == 2:
            instruction_text = "go    backward"
        elif instructions[i] == 3:
            instruction_text = "turn  left"
        elif instructions[i] == 4:
            instruction_text = "turn  right"

        print("Instruction " + str(i) + ":\t" + str(instructions[i]) + " ("+str(instruction_text)+")")


# prints out where heading changes are found in the step transitions list
# does not return anything
def heading_change_detection(step_transitions, robot_heading):
    # for n steps there are n-1 step transitions, so only iterate that far
    for i in range(len(found_path)-1):
        x_change  = step_transitions[i][0] - step_transitions[i-1][0] # get change in X between steps
        y_change  = step_transitions[i][1] - step_transitions[i-1][1] # get change in Y between steps

        # if there is indeed a heading change, 
        if x_change != step_transitions[i-1][0] and y_change != step_transitions[i-1][1]:
            # change heading accordingly, and
            if y_change == 1:
                if robot_heading != 4:
                    robot_heading += 1
                else:
                    robot_heading = 1
            elif y_change == -1:
                if robot_heading != 1:
                    robot_heading -= 1
                else:
                    robot_heading = 4
            elif x_change == 1:
                if robot_heading != 1:
                    robot_heading -= 1
                else:
                    robot_heading = 4
            elif x_change == -1:
                if robot_heading != 4:
                    robot_heading += 1
                else:
                    robot_heading = 1
            
            # print a notification of the detected heading change
            orientation = 0
            if robot_heading == 1:
                orientation = "North"
            elif robot_heading == 2:
                orientation = "East"
            elif robot_heading == 3:
                orientation = "South"
            elif robot_heading == 4:
                orientation = "West"
            print("heading change detected for step "+str(i)+"\t->\tstep "+str(i+1)+"! \theading "+orientation)

#######################################
### FOR TESTING a_star.py BY ITSELF ###
#######################################

if d_version == 1: # 16x10 version
    start          = start_location
    goal           = goal_location
    robot_heading  = initial_heading

    workspace = generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_grid(grid_columns, grid_rows, grid_obstacles, found_path)
elif d_version == 2: # 32 x 20 version
    start            = start_location_d
    goal             = goal_location_d
    robot_heading    = initial_heading

    workspace = generate_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, possible_locations_d)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_grid(grid_columns_d, grid_rows_d, grid_obstacles_d, found_path)
elif d_version == 0: # testing both
    # 16x10 version
    start          = start_location
    goal           = goal_location
    robot_heading  = initial_heading

    workspace = generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_grid(grid_columns, grid_rows, grid_obstacles, found_path)
    
    # 32 x 20 version
    start            = start_location_d
    goal             = goal_location_d
    robot_heading    = initial_heading

    workspace = generate_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, possible_locations_d)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_grid(grid_columns_d, grid_rows_d, grid_obstacles_d, found_path)
elif d_version == 3: # move forward 4 feet
    instructions = [1, 1, 1, 1] 
elif d_version == 4: # move forward 2 feet, turn left, move forward two feet
    instructions = [1, 1, 3, 1, 1] 
elif d_version == 5: # move forward 2 feet, turn right, move forward two feet
    instructions = [1, 1, 4, 1, 1] 
elif d_version == 6: # move forward 2 feet, turn left, move forward two feet, turn right, move forward two feet
    instructions = [1, 1, 3, 1, 1, 4, 1, 1]
elif d_version == 7: # turn left in a full circle
    instructions = [3, 3, 3, 3]
elif d_version == 8: # move forward 2 feet, do a left 180, move forward 2 feet
    instructions = [1, 1, 3, 3, 1, 1]




