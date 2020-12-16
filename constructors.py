import pygame
from buttonfunc import *
from elements import Button

def buttonConstructor():
    UIfont = pygame.font.SysFont("arial", 30)
    return [Button("Wall", UIfont, 50, 600, wallfunc),
        Button("Start", UIfont, 120, 600, startfunc),
        Button("End", UIfont, 200, 600, endfunc),
        Button("Forest", UIfont, 270, 600, forestfunc),
        Button("Start", UIfont, 600, 600, placeholder)]