from enums import CellState, color_array
from queue import Queue
from time import sleep
import pygame

def pathfinding(mouse, grid):
    #clear grid
    for row in grid:
        for cell in row:
            if cell.state >=5:
                cell.set_state(CellState["CLEAR"])
    #find start and endpoint
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j].state == CellState["START"]:
                start = [i, j]
            if grid[i][j].state == CellState["END"]:
                goal = [i, j]

    #pipe it into one of the algorithms
    if mouse.state == CellState["BREADTH"]:
        __breadthsearch(grid, start, goal)
    if mouse.state == CellState["DJ_ALGO"]:
        __djsearch(grid, start, goal)
    if mouse.state == CellState["GREEDY"]:
        __greedysearch(grid, start, goal)
    if mouse.state == CellState["ASTAR"]:
        __astarsearch(grid, start, goal)

def __neighbors(grid, current):
    possible_neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    neighbors = []
    for neighbor in possible_neighbors:
        #bounds detection
        if current[0] + neighbor[0] < 0 or current[0] + neighbor[0] > 109:
            continue
        if current[1] + neighbor[1] < 0 or current[1] + neighbor[1] > 199:
            continue
        #if wall
        if grid[current[0] + neighbor[0]][current[1] + neighbor[1]].state != CellState["WALL"]:
            neighbors.append([current[0] + neighbor[0], current[1] + neighbor[1]])
    
    return neighbors

    # return [[current[0] + 1, current[1]],
    #     [current[0] - 1, current[1]],
    #     [current[0], current[1] + 1],
    #     [current[0], current[1] - 1]
    # ]

def __breadthsearch(grid, start, goal):
    #init data structures
    #ALWAYS USE INDEXES! NEVER THE ACTUAL CELLS
    #TODO: VISUALISE (do this last)
    frontier = Queue()
    came_from = dict()
    frontier.put(start)
    came_from[str(start)] = None

    #main loop
    while not frontier.empty():
        current = frontier.get()

        #early exit condition
        if current == goal:
            break
        #color reached cell
        if grid[current[0]][current[1]].state != CellState["START"] and grid[current[0]][current[1]].state != CellState["END"]:
            grid[current[0]][current[1]].set_state(CellState["REACHED"])

        for neighbor in __neighbors(grid, current):
            if str(neighbor) not in came_from:
                #put in frontier
                frontier.put(neighbor)
                #color frontier
                if grid[neighbor[0]][neighbor[1]].state != CellState["START"] and grid[neighbor[0]][neighbor[1]].state != CellState["END"]:
                    grid[neighbor[0]][neighbor[1]].set_state(CellState["FRONTIER"])
                #put in came from
                came_from[str(neighbor)] = current
    
    #reconstruct path
    current = goal
    path = []
    while current != start:
        path.append(list(current))
        current = came_from[str(current)]
    path.append(start)
    path.reverse()
    #color path
    for index in path:
        if grid[index[0]][index[1]].state != CellState["START"] and grid[index[0]][index[1]].state != CellState["END"]:
            grid[index[0]][index[1]].set_state(CellState["PATH"])
    return path

def __djsearch(grid, start, goal):
    pass

def __greedysearch(grid, start, goal):
    pass

def __astarsearch(grid, start, goal):
    pass