import enum

class CellState(enum.Enum):
    CLEAR = 1
    WALL = 2
    FOREST = 3
    START = 4
    END = 5