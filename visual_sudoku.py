import pygame, sys, time
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

def find_empty_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

def check_column(board, col, num):
    for i in range(9):
        if board[i][col] == num:
            return False
    return True

def check_row(board, row, num):
    for i in range(9):
        if board[row][i] == num:
            return False
    return True

def check_box(board, xbox, ybox, num):
    for i in range(xbox * 3, (xbox * 3) + 3):
        for j in range(ybox * 3, (ybox * 3) + 3):
            if board[i][j] == num:
                return False
    return True

def simple_solver(board):
    emptyspace = find_empty_space(board)

    showNumbers(board)

    if emptyspace is None:
        return True

    for i in range(1, 10):
        ybox = emptyspace[1] // 3
        xbox = emptyspace[0] // 3
        if check_column(board, emptyspace[1], i) and check_row(board, emptyspace[0], i) and check_box(board, xbox, ybox, i):
            board[emptyspace[0]][emptyspace[1]] = i
            if simple_solver(board):
                return True
            board[emptyspace[0]][emptyspace[1]] = 0
    return False

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
    DISPLAYSURF.fill((255, 255, 255))
    makeGrid()

    for i in range(9):
        for j in range(9):
            text = font.render(str(board[j][i]), True, pygame.Color('black'))
            DISPLAYSURF.blit(text, (int(ninthwidth * i), int(ninthheight * j)))
    pygame.display.update()

# Takes click position on the board and gets the exact position of the number in that square
def clickPosition(origPosition):
    if origPosition[0] < DISPLAYWIDTH and origPosition[1] < DISPLAYHEIGHT:
        remainderX = origPosition[0] % ((DISPLAYWIDTH * 1.02) // 9)
        properX = origPosition[0] - remainderX
        remainderY = origPosition[1] % ((DISPLAYHEIGHT * 1.01) // 9)
        properY = origPosition[1] - remainderY

        xIndex = properX // ((DISPLAYWIDTH * 1.02) // 9)
        yIndex = properY // ((DISPLAYHEIGHT * 1.01) // 9)
        return int(xIndex), int(yIndex)

'''
# Takes a position and selects the correct number from the game board array
def selectNumber(position):
    xindex = position[0] // ((DISPLAYWIDTH * 1.02) // 9)
    yindex = position[1] // ((DISPLAYHEIGHT * 1.01) // 9)
    return int(xindex), int(yindex)
'''

def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT
    FPSCLOCK = pygame.time.Clock()
    global FPS
    FPS = 60
    pygame.init()
    DISPLAYWIDTH = 800
    DISPLAYHEIGHT = 600
    DISPLAYSURF  = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
    pygame.display.set_caption('Sudoku Solver')

    key = None
    selectedNumber = None
    #startTime = time.time()
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #playTime = round(time.time() - startTime)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    key = 0
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9

                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    key = 0

                gameBoard[selectedNumber[1]][selectedNumber[0]] = key

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                selectedNumber = clickPosition(position)
                #selectedNumber = selectNumber(correctPosition)
                key = None

        '''
        if board.selected and key != None:
            board.sketch(key)

        redraw_window(win, board, play_time, strikes)
        pygame.display.update()
        '''

        DISPLAYSURF.fill((255, 255, 255))
        makeGrid()
        showNumbers(gameBoard)
        #simple_solver(gameBoard)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()