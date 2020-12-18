import pygame
import enum

class CellState(enum.IntEnum):
    CLEAR = 0
    WALL = 1
    FOREST = 2
    START = 3
    END = 4
    FRONTIER = 5
    REACHED = 6
    PATH = 7

    #below are states for triggering visualisation functions
    #these are all mouse only
    #this is disgusting, but it'll have to do for now
    SEARCH_FINISHED = 9
    BREADTH = 10
    DJ_ALGO = 11
    GREEDY = 12
    ASTAR = 13
    

color_array = [
    pygame.color.THECOLORS["white"],
    pygame.color.THECOLORS["black"],
    pygame.color.THECOLORS["green"],
    pygame.color.THECOLORS["red"],
    pygame.color.THECOLORS["blue"],
    pygame.color.THECOLORS["chartreuse1"],
    pygame.color.THECOLORS["chartreuse4"],
    pygame.color.THECOLORS["darkviolet"],
]