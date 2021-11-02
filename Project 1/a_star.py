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

# A* code from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

# Above license applies to all code in this repository, 
# not just the code borrowed from Red Blob Games.

###############
### IMPORTS ###
###############

import math as math
import heapq

from specification import *

#################
### FUNCTIONS ###
#################

class Workspace:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.walls = []
        self.weights = {}

    def cost(self, from_node, to_node) -> float:
        return self.weights.get(to_node, 1)
    
    def in_bounds(self, id) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id) -> bool:
        return id not in self.walls
    
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

# priority queue object for all the different searches
# used in a_star_search
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# rebuilds the path found by a_star_search() as an ordered list of positions 
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse()     # optional
    return path

# manhattan distance heuristic
def manhattan_heuristic(a, b) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# pathfinding with A*, using manhattan distance heuristic
def a_star_search(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put(start, 0)
    came_from = {}
    cost_so_far = {}
    came_from[start] = None
    cost_so_far[start] = 0
    
    while not frontier.empty():
        current = frontier.get()
        
        if current == goal:
            break
        
        for next in graph.neighbors(current):
            new_cost = cost_so_far[current] + graph.cost(current, next)
            if next not in cost_so_far or new_cost < cost_so_far[next]:
                cost_so_far[next] = new_cost
                priority = new_cost + manhattan_heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far

# Draws the workspace grid with obstacles and path
def draw_workspace(grid_columns, grid_rows, grid_obstacles, found_path):
    grid_list = []
    grid_print = ""
    item_count = 0

    print("___" * grid_columns)
    for y in range(grid_rows):
        for x in range(grid_columns):
            if (x, y) in found_path:
                grid_list.append(" @ ")
                item_count += 1
            elif (x, y) in grid_obstacles:
                grid_list.append("[X]")
                item_count += 1
            else:
                grid_list.append(" . ")
                item_count += 1

            if item_count == grid_columns:
                grid_list.append("\n")
                item_count = 0
    
    for string in grid_list:
        grid_print += string
    print(grid_print)
    print("~~~" * grid_columns)

# generates and returns a workspace divided into 1' x 1' cells with obstacles marked
def generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations):
    workspace         = Workspace(grid_columns, grid_rows)
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
        xy_change = [x_change, y_change]                  # create temp list, 0th item = X change, 1st item = Y change
        step_transitions.append(xy_change)                # append temp list to the list of all step transitions

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


#######################################
### FOR TESTING a_star.py BY ITSELF ###
#######################################

if d_version == 0: # testing both
    # 16x10 version
    start          = start_location
    goal           = goal_location
    robot_heading  = initial_heading

    workspace = generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_workspace(grid_columns, grid_rows, grid_obstacles, found_path)
    
    # 32 x 20 version
    start            = start_location_d
    goal             = goal_location_d
    robot_heading    = initial_heading

    workspace = generate_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, possible_locations_d)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, found_path)
elif d_version == 1: # 16x10 version
    start          = start_location
    goal           = goal_location
    robot_heading  = initial_heading

    workspace = generate_workspace(grid_columns, grid_rows, grid_obstacles, possible_locations)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_workspace(grid_columns, grid_rows, grid_obstacles, found_path)
elif d_version == 2: # 32 x 20 version
    start            = start_location_d
    goal             = goal_location_d
    robot_heading    = initial_heading

    workspace = generate_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, possible_locations_d)
    came_from, cost_so_far = a_star_search(workspace, start, goal)

    found_path       = reconstruct_path(came_from, start=start, goal=goal)
    step_transitions = get_step_transitions(found_path)
    instructions     = get_instructions(step_transitions)

    draw_workspace(grid_columns_d, grid_rows_d, grid_obstacles_d, found_path)
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
else:
    pass




