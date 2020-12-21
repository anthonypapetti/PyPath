from enums import CellState, color_array
from queue import Queue, PriorityQueue
from time import sleep
import pygame
from dataclasses import dataclass, field

@dataclass
class PriorityIndex:
    priority: int
    index: list() = field(compare=False)

    def __lt__(self, other):
        return self.priority < other.priority

def pathfinding(mouse, grid):
    #clear grid
    for row in grid.cells:
        for cell in row:
            if cell.state >=5:
                cell.set_state(CellState["CLEAR"])
    #find start and endpoint
    for i in range(len(grid.cells)):
        for j in range(len(grid.cells[i])):
            if grid.cells[i][j].state == CellState["START"]:
                start = [i, j]
            if grid.cells[i][j].state == CellState["END"]:
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
    #init data structures
    #ALWAYS USE INDEXES! NEVER THE ACTUAL CELLS
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
        if grid.cells[current[0]][current[1]].state != CellState["START"] and grid.cells[current[0]][current[1]].state != CellState["END"]:
            grid.cells[current[0]][current[1]].set_state(CellState["REACHED"])

        for neighbor in grid.neighbors(current):
            if str(neighbor) not in came_from:
                #put in frontier
                frontier.put(neighbor)
                #color frontier
                if grid.cells[neighbor[0]][neighbor[1]].state != CellState["START"] and grid.cells[neighbor[0]][neighbor[1]].state != CellState["END"]:
                    grid.cells[neighbor[0]][neighbor[1]].set_state(CellState["FRONTIER"])
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
        if grid.cells[index[0]][index[1]].state != CellState["START"] and grid.cells[index[0]][index[1]].state != CellState["END"]:
            grid.cells[index[0]][index[1]].set_state(CellState["PATH"])
    return path

def __djsearch(grid, start, goal):
    #BUG: PriorityQueue is sorting by x value, need dataclasses
    frontier = PriorityQueue()
    came_from = dict()
    cost_so_far = dict()
    frontier.put(PriorityIndex(0, start))
    came_from[str(start)] = None
    cost_so_far[str(start)] = 0

    #main loop
    while not frontier.empty():
        current = frontier.get().index

        #early exit condition
        if current == goal:
            break
        
        #color reached cell
        if grid.cells[current[0]][current[1]].state != CellState["START"] and grid.cells[current[0]][current[1]].state != CellState["END"]:
            grid.cells[current[0]][current[1]].set_state(CellState["REACHED"])

        for neighbor in grid.neighbors(current):
            new_cost = cost_so_far[str(current)] + grid.cost(neighbor)
            if str(neighbor) not in cost_so_far or new_cost < cost_so_far[str(neighbor)]:
                #add to frontier
                frontier.put(PriorityIndex(new_cost, neighbor))
                #color frontier
                if grid.cells[neighbor[0]][neighbor[1]].state != CellState["START"] and grid.cells[neighbor[0]][neighbor[1]].state != CellState["END"]:
                    grid.cells[neighbor[0]][neighbor[1]].set_state(CellState["FRONTIER"])
                #put in reference dictionaries
                cost_so_far[str(neighbor)] = new_cost
                came_from[str(neighbor)] = current
    
    #reconstruct path
    current = goal
    path = []
    while current != start:
        path.append(list(current))
        current = came_from[str(current)]
    path.append(start)
    path.reverse()
    for index in path:
        if grid.cells[index[0]][index[1]].state != CellState["START"] and grid.cells[index[0]][index[1]].state != CellState["END"]:
            grid.cells[index[0]][index[1]].set_state(CellState["PATH"])
    return path

def __greedysearch(grid, start, goal):
    pass

def __astarsearch(grid, start, goal):
    pass