import pygame
from enums import *

class Border():
    def __init__(self, posx, posy):
        self.image = pygame.Surface((1000, 5))
        self.image.fill((201,201,201))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
    
    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

class Button():
    def __init__(self, text, font, posx, posy, onclick):
        self.image = font.render(text, True, (0, 0, 0), (201,201,201))
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy
        self.onclick = onclick
    
    #draws buttons onto the screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

class MouseHandler():
    def __init__(self):
        self.position = pygame.mouse.get_pos()
        self.state = CellState["WALL"]
    
    #checks for clicks
    def __click(self, rect):
        if self.position[0] > rect.topleft[0] and self.position[0] < rect.topright[0]:
            if self.position[1] > rect.topleft[1] and self.position[1] < rect.bottomleft[1]:
                return True
    
    def right_click(self, grid):
        for row in grid:
            for cell in row:
                if self.__click(cell.rect):
                    if cell.state not in [CellState["START"], CellState["END"]]:
                        cell.set_state(CellState["CLEAR"])

    def left_click(self, grid, buttons):
        #check for grid clear
        if self.state == CellState["SEARCH_FINISHED"]:
            for row in grid:
                for cell in row:
                    if cell.state >=5:
                        cell.set_state(CellState["CLEAR"])
        #check for painting
        for row in grid:
            for cell in row:
                if self.__click(cell.rect):
                    #painting walls/forest
                    if self.state in [1, 2]:
                        if cell.state not in [3, 4]:
                            cell.set_state(self.state)
                    #changing position of start/end
                    if self.state in [3, 4]:
                        #get rid of old start/end
                        for searchrow in grid:
                            for searchcell in searchrow:
                                if searchcell.state == self.state:
                                    searchcell.set_state(CellState["CLEAR"])
                        #add new start/end
                        cell.set_state(self.state)
                                
        #check for buttons
        for button in buttons:
            if self.__click(button.rect):
                self.state = button.onclick()