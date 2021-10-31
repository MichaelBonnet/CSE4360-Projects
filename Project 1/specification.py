# This file exists for defining the facts of the workspace, goals, etc.
# Change these variables to change what happens in a_star.py and main.py to figure out a path.
# To help visualize the workspace.
# 0 = empty cell
# X = obstacle cell
# S = start
# G = goal
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

start_location = (0,  5)
goal_location  = (12, 4)

grid_columns   = 16
grid_rows      = 10

possible_locations = []
for j in range(grid_columns):
    for i in range(grid_rows):
        possible_locations.append((j, i))

# Headings:
# North (+Y) = 1
# East  (+X) = 2
# South (-Y) = 3
# West  (-X) = 4
initial_heading = 2

grid_obstacles = [
                 # Obstacle 1 - 3x2
                 (1, 1), (2, 1), (1, 2), (2, 2), (3, 1), (3, 2),
                 # Obstacle 2 - 3x3
                 (0, 7), (1, 7), (2, 7), (0, 8), (1, 8), (2, 8), (0, 9), (1, 9), (2, 9),
                 # Obstacle 3 - 2x4
                 (5, 3), (6, 3), (5, 4), (6, 4), (5, 5), (6, 5), (5, 6), (6, 6),
                 # Obstacle 4 - 2x2
                 (8, 3), (9, 3), (8, 4), (9, 4),
                 # Obstacle 5 - 1x1
                 (5, 0),
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