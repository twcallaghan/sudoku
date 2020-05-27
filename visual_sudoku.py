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

# Shows if there was a number there originally, thus the user can't get rid of it
booleanBoard = [
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False],
    [False, False, False, False, False, False, False, False, False]
]

def fillBooleanBoard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                booleanBoard[i][j] = True

def find_empty_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j

def check_column(board, col, num, ignorePos):
    for i in range(9):
        if board[i][col] == num and (i, col) != ignorePos:
            return False
    return True

def check_row(board, row, num, ignorePos):
    for i in range(9):
        if board[row][i] == num and (row, i) != ignorePos:
            return False
    return True

def check_box(board, xbox, ybox, num, ignorePos):
    for i in range(xbox * 3, (xbox * 3) + 3):
        for j in range(ybox * 3, (ybox * 3) + 3):
            if board[i][j] == num and (i, j) != ignorePos:
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
        if check_column(board, emptyspace[1], i, None) and check_row(board, emptyspace[0], i, None) and check_box(board, xbox, ybox, i, None):
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

# Takes click position on the board and gets the exact position of the number in that square in terms of index
def clickPosition(origPosition):
    if origPosition[0] < DISPLAYWIDTH and origPosition[1] < DISPLAYHEIGHT:
        remainderX = origPosition[0] % ((DISPLAYWIDTH * 1.02) // 9)
        properX = origPosition[0] - remainderX
        remainderY = origPosition[1] % ((DISPLAYHEIGHT * 1.01) // 9)
        properY = origPosition[1] - remainderY

        xIndex = properX // ((DISPLAYWIDTH * 1.02) // 9)
        yIndex = properY // ((DISPLAYHEIGHT * 1.01) // 9)
        return int(xIndex), int(yIndex)

def validBoard(board):
    for i in range(9):
        for j in range(9):
            ybox = j // 3
            xbox = i // 3
            if check_column(board, j, board[i][j], (i, j)) and check_row(board, i, board[i][j], (i, j)) and check_box(board, xbox, ybox, board[i][j], (i, j)):
                continue
            else:
                print("Invalid board")
                return False
    print("Valid board. Awesome!")
    return True

def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, FPS
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    pygame.init()
    DISPLAYWIDTH = 800
    DISPLAYHEIGHT = 600
    DISPLAYSURF  = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
    pygame.display.set_caption('Sudoku Solver')

    key = None
    selectedNumber = None
    #startTime = time.time()

    fillBooleanBoard(gameBoard)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            #playTime = round(time.time() - startTime)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0 or event.key:
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

                if selectedNumber is not None and not booleanBoard[selectedNumber[1]][selectedNumber[0]]:
                    gameBoard[selectedNumber[1]][selectedNumber[0]] = key
                else:
                    key = None

                if event.key == pygame.K_SPACE:
                    key = None
                    simple_solver(gameBoard)

                if event.key == pygame.K_c and find_empty_space(gameBoard) is None:
                    print('here')
                    font = pygame.font.SysFont("Arial", 50)
                    isValid = validBoard(gameBoard)
                    if isValid is True:
                        text = font.render("Congratulations! You win!", True, pygame.Color('red'))
                        DISPLAYSURF.blit(text, (int(DISPLAYWIDTH // 6), int(DISPLAYHEIGHT // 4)))
                        pygame.display.update()
                        time.sleep(5)
                        pygame.quit()
                        sys.exit()
                    else:
                        text = font.render("Oh no! Your Board is incorrect!", True, pygame.Color('red'))
                        DISPLAYSURF.blit(text, (int(DISPLAYWIDTH // 6), int(DISPLAYHEIGHT // 4)))
                        pygame.display.update()
                        time.sleep(5)

            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                selectedNumber = clickPosition(position)
                key = None


        makeGrid()
        showNumbers(gameBoard)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()