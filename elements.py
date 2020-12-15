import pygame

class Cell():
    def __init__(self, posx, posy):
        self.image = pygame.Surface((5, 5))
        self.image.fill((255, 255, 255))
        self.color = (255, 255, 255)
        self.rect = self.image.get_rect()
        self.rect.x = posx
        self.rect.y = posy

    #draws onto screen
    def Draw(self, surface):
        surface.blit(self.image, self.rect)

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
        self.state = "WALL"
    
    #checks for clicks
    def __click(self, rect):
        if self.position[0] > rect.topleft[0] and self.position[0] < rect.topright[0]:
            if self.position[1] > rect.topleft[1] and self.position[1] < rect.bottomleft[1]:
                return True
    
    def left_click(self, grid, buttons):
        for row in grid:
            for cell in row:
                if self.__click(cell.rect):
                    if self.state == "WALL":
                        cell.image.fill(pygame.color.THECOLORS["black"])
                        cell.color = pygame.color.THECOLORS["black"]