import pygame
from enums import CellState, color_array

class Grid():
    def __init__(self, cellsize):
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
        self.cells = grid
    
    #finds cost of cell at index
    def cost(self, index):
        if self.cells[index[0]][index[1]].state == CellState["FOREST"]:
            return 4
        else:
            return 1

    #finds neighbors of cell at index
    def neighbors(self, index):
        possible_neighbors = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        neighbors = []
        for neighbor in possible_neighbors:
            #bounds detection
            if index[0] + neighbor[0] < 0 or index[0] + neighbor[0] > 109:
                continue
            if index[1] + neighbor[1] < 0 or index[1] + neighbor[1] > 199:
                continue
            #if wall
            if self.cells[index[0] + neighbor[0]][index[1] + neighbor[1]].state != CellState["WALL"]:
                neighbors.append([index[0] + neighbor[0], index[1] + neighbor[1]])
        
        return neighbors
    
    #sets the state of a cell at an index
    def path_state(self, index, state):
        if self.cells[index[0]][index[1]].state != CellState["START"] and self.cells[index[0]][index[1]].state != CellState["END"]:
            self.cells[index[0]][index[1]].set_state(state)

class Cell():
    def __init__(self, posx, posy):
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.state = CellState["CLEAR"]

    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)
    
    #take in a CellState and sets state and fills with color
    def set_state(self, state):
        self.state = state
        self.image.fill(color_array[state])