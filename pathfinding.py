from enums import CellState
from queue import Queue

def pathfinding(mouse, grid):
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

def __breadthsearch(grid, start, goal):
    pass

def __djsearch(grid, start, goal):
    pass

def __greedysearch(grid, start, goal):
    pass

def __astarsearch(grid, start, goal):
    pass