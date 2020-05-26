import pygame, sys
from pygame.locals import *

gameBoard = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0],
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

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

def showNumbers(board):
    ninthwidth = (DISPLAYWIDTH * 1.02) // 9
    ninthheight = (DISPLAYHEIGHT * 1.01) // 9

    font = pygame.font.SysFont("Arial", 36)

    for i in range(9):
        for j in range(9):
            text = font.render(str(board[j][i]), True, pygame.Color('black'))
            DISPLAYSURF.blit(text, (int(ninthwidth * i), int(ninthheight * j)))

def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    pygame.init()
    DISPLAYWIDTH = 800
    DISPLAYHEIGHT = 600
    DISPLAYSURF  = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
    pygame.display.set_caption('Sudoku Solver')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        DISPLAYSURF.fill((255, 255, 255))
        makeGrid()
        showNumbers(gameBoard)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()