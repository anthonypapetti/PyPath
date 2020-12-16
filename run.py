import pygame
from pygame.locals import *
from elements import Border, MouseHandler
from constructors import *

#initialize pygame
pygame.init()
pygame.display.set_caption("PyPath")

#initialize screen and handlers
size = (1000, 700)
cellsize = (int(size[0]/5), int(550/5))
screen = pygame.display.set_mode(size)
screen.fill(pygame.color.THECOLORS["white"])
mouse = MouseHandler()

#initalize buttons/UI
buttons = buttonConstructor()
UIfont = pygame.font.SysFont("arial", 30)
MapText = UIfont.render("Create Map:", True, (0, 0, 0))
VisText = UIfont.render("Visualisation:", True, (0, 0, 0))
border = Border(0, 550)

#intialize cell grid
grid = gridConstructor(cellsize)

pygame.display.update()
#main loop
run = True
while run:
    mouse.position = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        #left click
        if pygame.mouse.get_pressed()[0]:
            mouse.left_click(grid, buttons)
        #right click
        if pygame.mouse.get_pressed()[2]:
            mouse.right_click(grid)
    
    #drawing goes below here
    #draw cell grid
    for row in grid:
        for cell in row:
            cell.Draw(screen)
    border.Draw(screen)

    #draw buttons
    for button in buttons:
        button.Draw(screen)
    
    #draw text
    screen.blit(MapText, (125, 560))
    screen.blit(VisText, (650, 560))
    
    #update display
    pygame.display.update()

pygame.quit()