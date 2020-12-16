import pygame
import enum

class CellState(enum.IntEnum):
    CLEAR = 0
    WALL = 1
    FOREST = 2
    START = 3
    END = 4

color_array = [
    pygame.color.THECOLORS["white"],
    pygame.color.THECOLORS["black"],
    pygame.color.THECOLORS["green"],
    pygame.color.THECOLORS["red"],
    pygame.color.THECOLORS["blue"]
]