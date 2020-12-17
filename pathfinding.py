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
        print(__breadthsearch(grid, start, goal))
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

        for neighbor in __neighbors(grid, current):
            if str(neighbor) not in came_from:
                frontier.put(neighbor)
                came_from[str(neighbor)] = current
    
    #TODO: RECONSTRUCT PATH
    current = goal
    path = []
    while current != start:
        path.append(list(current))
        current = came_from[str(current)]
    path.append(start)
    path.reverse()
    return path

def __djsearch(grid, start, goal):
    pass

def __greedysearch(grid, start, goal):
    pass

def __astarsearch(grid, start, goal):
    pass