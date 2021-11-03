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

# This file exists for defining the facts of the workspace, goals, etc.
# Change these variables to change what happens in a_star.py and main.py to figure out a path.

###############
### IMPORTS ###
###############

import math as math

#############
### SPECS ###
#############

d_version = 2

# parameters for wheel stuff
if d_version == 1:
    wheel_diameter          = 69
    wheel_circumference     = wheel_diameter * math.pi
    circumferences_per_foot = 305 / wheel_circumference
    total_degrees_per_foot  = circumferences_per_foot * 360  
if d_version == 2:
    wheel_diameter          = 69
    wheel_circumference     = wheel_diameter * math.pi
    circumferences_per_foot = 305 / wheel_circumference
    total_degrees_per_foot  = (circumferences_per_foot * 360)/2

if d_version == 1:
    grid_columns     = 16
    grid_rows        = 10
if d_version == 2:
    grid_columns     = 32
    grid_rows        = 20

possible_locations = []
for i in range(grid_rows):
    for j in range(grid_columns):
        possible_locations.append((i, j))

# To help visualize the workspace.
# 0 = empty cell
# X = obstacle cell
# S = start
# G = goal

#####################
### 16x10 version ###
#####################

# maze = [
#         [0, 0, 0, 0, 0, 0, X, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, X, X, 0, X, X, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, X, X, 0, X, X, 0, 0, G, 0, 0, 0],
#         [S, 0, 0, 0, 0, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#         [X, X, X, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
# ]

# start_location = (0,  5)
# goal_location  = (12, 4)

# start_location = (0,  4)
# goal_location  = (12, 5)

start_location = (4,  0)
goal_location  = (5, 12)

# grid_columns   = 16
# grid_rows      = 10

# possible_locations = []
# for i in range(grid_rows):
#     for j in range(grid_columns):
#         possible_locations.append((i, j))

# for location in possible_locations:
#     print(location)

# possible_locations = []
# for j in range(grid_rows):
#     for i in range(grid_columns):
#         possible_locations.append((j, i))

# Headings:
# North (+Y) = 1
# East  (+X) = 2
# South (-Y) = 3
# West  (-X) = 4
grid_obstacles = [
                 # Obstacle 1 - 3x2
                 (7, 1), (7, 2), (7, 3), (6, 1), (6, 2), (6, 3),
                 # Obstacle 2 - 3x3
                 (0, 0), (0, 1), (0, 2), 
                 (1, 0), (1, 1), (1, 2),
                 (2, 0), (2, 1), (2, 2),
                 # Obstacle 3 - 2x4
                 (3, 5), (3, 6),
                 (4, 5), (4, 6),
                 (5, 5), (5, 6),
                 (6, 5), (6, 6),
                 # Obstacle 4 - 2x2
                 (5, 9), (5, 10),
                 (6, 9), (6, 10),
                 # Obstacle 5 - 1x1
                 (9, 7),
                #  # Obstacle 1 - 3x2
                #  (1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (3, 2),
                #  # Obstacle 2 - 3x3
                #  (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8), (0, 9), (1, 9), (2, 9),
                #  # Obstacle 3 - 2x4
                #  (5, 3), (6, 3), (5, 4), (6, 4), (5, 5), (6, 5), (5, 6), (6, 6),
                #  # Obstacle 4 - 2x2
                #  (8, 3), (9, 3), (8, 4), (9, 4),
                #  # Obstacle 5 - 1x1
                #  (5, 0),
                 # Obstacle 6 - MxN
                 # Obstacle 7 - MxN
                 # Obstacle 8 - MxN
                 # Obstacle 9 - MxN
                 # Obstacle 10 - MxN
                 # Obstacle 11 - MxN
                 # Obstacle 12 - MxN
                 # Obstacle 13 - MxN
                 # Obstacle 14 - MxN
                 # Obstacle 15 - MxN
                 # Obstacle 16 - MxN
                 # Obstacle 17 - MxN
                 # Obstacle 18 - MxN
                 # Obstacle 19 - MxN
                 # Obstacle 20 - MxN
                 # Obstacle 21 - MxN
                 # Obstacle 22 - MxN
                 # Obstacle 23 - MxN
                 # Obstacle 24 - MxN
                 # Obstacle 25 - MxN
] 

#####################
### 32x20 version ###
#####################

# maze = [     0   1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31
#         19 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         18 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         17 [ 0,  0,  X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         16 [ 0,  0,  X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         15 [ 0,  0,  X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         14 [ 0,  0,  X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         13 [ 0,  0,  X,  X,  X,  X,  X,  X,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         12 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         11 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#         10 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0, {G}, 0,  0,  0,  0,  0,  0 ]
#          9 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          8 [{S}, 0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          7 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          6 [ 0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          5 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          4 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          3 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          2 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          1 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
#          0 [ X,  X,  X,  X,  X,  X,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0 ]
# ]

start_location_d = (11, 0)
goal_location_d  = (9, 25)

# grid_columns_d   = 32
# grid_rows_d      = 20

# possible_locations_d = []
# for i in range(grid_rows_d):
#     for j in range(grid_columns_d):
#         possible_locations_d.append((i, j))

# possible_locations = []
# for i in range(grid_rows):
#     for j in range(grid_columns):
#         possible_locations.append((i, j))

# Headings:
# North (+Y) = 1
# East  (+X) = 2
# South (-Y) = 3
# West  (-X) = 4
initial_heading = 2

grid_obstacles_d = [
                    # Obstacle 1 - 6x4 done
                    (17, 2), (17, 3), (17, 4), (17, 5), (17, 6), (17, 7),
                    (16, 2), (16, 3), (16, 4), (16, 5), (16, 6), (16, 7),
                    (15, 2), (15, 3), (15, 4), (15, 5), (15, 6), (15, 7),
                    (14, 2), (14, 3), (14, 4), (14, 5), (14, 6), (14, 7),
                    # Obstacle 2 - 6x6 done
                    (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6),
                    (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6),
                    (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6),
                    (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6),
                    (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6),
                    (0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6),
                    # Obstacle 3 - 4x8 done
                    (13, 10), (13, 11), (13, 12), (13, 13),
                    (12, 10), (12, 11), (12, 12), (12, 13),
                    (11, 10), (11, 11), (11, 12), (11, 13),
                    (10, 10), (10, 11), (10, 12), (10, 13),
                    (9, 10), (9, 11), (9, 12), (9, 13),
                    (8, 10), (8, 11), (8, 12), (8, 13),
                    (7, 10), (7, 11), (7, 12), (7, 13),
                    (6, 10), (6, 11), (6, 12), (6, 13),
                    # Obstacle 4 - 4x4 doe
                    (13, 18), (13, 19), (13, 20), (13, 21),
                    (12, 18), (12, 19), (12, 20), (12, 21),
                    (11, 18), (11, 19), (11, 20), (11, 21),
                    (10, 18), (10, 19), (10, 20), (10, 21),
                    # Obstacle 5 - 2x2 done
                    (19, 12), (19, 13),
                    (18, 12), (18, 13),
                    # Obstacle 6 - MxN
                    # Obstacle 7 - MxN
                    # Obstacle 8 - MxN
                    # Obstacle 9 - MxN
                    # Obstacle 10 - MxN
                    # Obstacle 11 - MxN
                    # Obstacle 12 - MxN
                    # Obstacle 13 - MxN
                    # Obstacle 14 - MxN
                    # Obstacle 15 - MxN
                    # Obstacle 16 - MxN
                    # Obstacle 17 - MxN
                    # Obstacle 18 - MxN
                    # Obstacle 19 - MxN
                    # Obstacle 20 - MxN
                    # Obstacle 21 - MxN
                    # Obstacle 22 - MxN
                    # Obstacle 23 - MxN
                    # Obstacle 24 - MxN
                    # Obstacle 25 - MxN
]
