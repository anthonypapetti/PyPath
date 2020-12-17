import pygame
from buttonfunc import *
from elements import Button, Cell
from enums import CellState, color_array

def buttonConstructor():
    UIfont = pygame.font.SysFont("arial", 30)
    return [Button("Wall", UIfont, 50, 620, wallfunc),
        Button("Start", UIfont, 120, 620, startfunc),
        Button("End", UIfont, 200, 620, endfunc),
        Button("Forest", UIfont, 270, 620, forestfunc),
        Button("Breadth", UIfont, 550, 620, breadthbutton),
        Button("DJ", UIfont, 675, 620, djbutton),
        Button("Greedy", UIfont, 725, 620, greedybutton),
        Button("A*", UIfont, 850, 620, astarbutton),
        ]

def gridConstructor(cellsize):
    grid = []
    xptr = 0
    yptr = 0
    for i in range(cellsize[1]):
        row = []
        for j in range(cellsize[0]):
            row.append(Cell(xptr, yptr))
            xptr += 5
        yptr += 5
        xptr = 0
        grid.append(row)
    #default start/ends
    grid[0][0].image.fill(color_array[CellState(3)])
    grid[0][0].state = CellState(3)
    grid[-1][-1].image.fill(color_array[CellState(4)])
    grid[-1][-1].state = CellState(4)
    return grid