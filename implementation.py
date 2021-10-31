# Code taken from or modified from https://www.redblobgames.com/pathfinding/a-star/
# Copyright 2014 Red Blob Games <redblobgames@gmail.com>
#
# Feel free to use this code in your own projects, including commercial projects
# License: Apache v2.0 <http://www.apache.org/licenses/LICENSE-2.0.html>

###############
### IMPORTS ###
###############

import heapq

#################
### FUNCTIONS ###
#################

def draw_grid(grid_columns, grid_rows, grid_obstacles, found_path):
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

class SquareGrid:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        #self.walls: List[GridLocation] = []
        self.walls = []
    
    def in_bounds(self, id) -> bool:
        (x, y) = id
        return 0 <= x < self.width and 0 <= y < self.height
    
    def passable(self, id) -> bool:
        return id not in self.walls
    
    # def neighbors(self, id: GridLocation) -> Iterator[GridLocation]:
    def neighbors(self, id):
        (x, y) = id
        neighbors = [(x+1, y), (x-1, y), (x, y-1), (x, y+1)] # E W N S
        # see "Ugly paths" section for an explanation:
        if (x + y) % 2 == 0: neighbors.reverse() # S N W E
        results = filter(self.in_bounds, neighbors)
        results = filter(self.passable, results)
        return results

# Extends SquareGrid to add weights
class GridWithWeights(SquareGrid):
    def __init__(self, width: int, height: int):
        super().__init__(width, height)
        # self.weights: Dict[GridLocation, float] = {}
        self.weights = {}
    
    def cost(self, from_node, to_node) -> float:
        return self.weights.get(to_node, 1)

class Graph:
    def neighbors(self, id): pass

class WeightedGraph(Graph):
    def cost(self, from_id, to_id) -> float: pass

# thanks to @m1sp <Jaiden Mispy> for this simpler version of
# reconstruct_path that doesn't have duplicate entries
def reconstruct_path(came_from, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = came_from[current]
    path.append(start) # optional
    path.reverse()     # optional
    return path

# priority queue object for all the different searches
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self) -> bool:
        return not self.elements
    
    def put(self, item, priority: float):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

# manhattan distance heuristic
def heuristic(a, b) -> float:
    (x1, y1) = a
    (x2, y2) = b
    return abs(x1 - x2) + abs(y1 - y2)

# pathfinding with A*
def a_star_search(graph: WeightedGraph, start, goal):
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
                priority = new_cost + heuristic(next, goal)
                frontier.put(next, priority)
                came_from[next] = current
    
    return came_from, cost_so_far
