import pygame
from buttonfunc import *
from ui import Button
from enums import CellState, color_array

def buttonConstructor():
    UIfont = pygame.font.SysFont("arial", 30)
    return [Button("Wall", UIfont, 50, 620, wallfunc),
        Button("Start", UIfont, 120, 620, startfunc),
        Button("End", UIfont, 200, 620, endfunc),
        Button("Forest", UIfont, 270, 620, forestfunc),
        Button("CLEAR", UIfont, 410, 620, clearbutton),
        Button("Breadth", UIfont, 550, 620, breadthbutton),
        Button("DJ", UIfont, 675, 620, djbutton),
        Button("Greedy", UIfont, 725, 620, greedybutton),
        Button("A*", UIfont, 850, 620, astarbutton),
        ]