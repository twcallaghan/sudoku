import pygame, sys
from pygame.locals import *

def makeGrid():
    thirdwidth = DISPLAYWIDTH // 3
    thirdheight = DISPLAYHEIGHT // 3

    #black bigger boxes
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(DISPLAYSURF, pygame.Color('black'), pygame.Rect((thirdwidth * i), (thirdheight * j), thirdwidth, thirdheight), 1)

    #smaller gray boxes
    ninthwidth = (thirdwidth + 1) // 3
    ninthheight = (thirdheight + 1) // 3
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(DISPLAYSURF, pygame.Color('gray'), pygame.Rect((ninthwidth * i), (ninthheight * j), ninthwidth, ninthheight), 1)

def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    pygame.init()
    DISPLAYWIDTH = 800
    DISPLAYHEIGHT = 600
    DISPLAYSURF  = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
    pygame.display.set_caption('Testing')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill((255, 255, 255))
        makeGrid()
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()