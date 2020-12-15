import pygame
from pygame.locals import *
from elements import *
from buttonfunc import *

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
UIfont = pygame.font.SysFont("arial", 30)
buttons = [Button("Wall", UIfont, 50, 600, placeholder), Button("Start", UIfont, 120, 600, placeholder), Button("End", UIfont, 200, 600, placeholder), Button("Forest", UIfont, 270, 600, placeholder), Button("Start", UIfont, 600, 600, placeholder)]
border = Border(0, 550)

#intialize cell grid
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
            print("yaay")
    
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