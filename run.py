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
border = Border(0, 550)

#intialize cell grid
grid = gridConstructor(cellsize)
print(len(grid))
print(len(grid[0]))

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
    
    #update display
    pygame.display.update()

pygame.quit()