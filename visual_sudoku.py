import pygame
import sys
import time
from pygame.locals import *
import board_generator

global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, FPS
global gameboard

# Sudoku game board to be used in the game
'''
gameboard = [
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
'''

# Shows if there was a number there originally, thus the user can't get rid of it
booleanboard = [
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


# Fills the boolean board according to the gameboard
def fillbooleanboard(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] != 0:
                booleanboard[i][j] = True


# Finds the next empty space in the board (rows before cols)
def find_empty_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j


# Checks the column to see if the number attempting to be inserted is already there
def check_column(board, col, num, ignorepos):
    for i in range(9):
        if board[i][col] == num and (i, col) != ignorepos:
            return False
    return True


# See check_column, same thing but with the row
def check_row(board, row, num, ignorepos):
    for i in range(9):
        if board[row][i] == num and (row, i) != ignorepos:
            return False
    return True


# Checks the box that the attempted insertion is happening in to see if the number is already there
def check_box(board, xbox, ybox, num, ignorepos):
    for i in range(xbox * 3, (xbox * 3) + 3):
        for j in range(ybox * 3, (ybox * 3) + 3):
            if board[i][j] == num and (i, j) != ignorepos:
                return False
    return True


# Solves the sudoku board with backtracking given there is a solution
def simple_solver(board):
    emptyspace = find_empty_space(board)

    # Makes the algorithm visible on the board
    shownumbers(board)

    # Base case for recursion
    if emptyspace is None:
        return True

    for i in range(1, 10):
        # Getting sudoku boxes
        ybox = emptyspace[1] // 3
        xbox = emptyspace[0] // 3
        if check_column(board, emptyspace[1], i, None) and check_row(board, emptyspace[0], i, None) and \
                check_box(board, xbox, ybox, i, None):
            board[emptyspace[0]][emptyspace[1]] = i
            # Recursive call that allows for basically infinite recursion until a solution is found
            if simple_solver(board):
                return True
            board[emptyspace[0]][emptyspace[1]] = 0
    # If no solution
    return False


# Makes the graphical grid out of rectangles
def makegrid():
    thirdwidth = DISPLAYWIDTH // 3
    thirdheight = DISPLAYHEIGHT // 3

    # black bigger boxes
    for i in range(3):
        for j in range(3):
            pygame.draw.rect(DISPLAYSURF, pygame.Color('black'),
                             pygame.Rect((thirdwidth * i), (thirdheight * j), thirdwidth, thirdheight), 1)

    # smaller gray boxes
    ninthwidth = (thirdwidth + 1) // 3
    ninthheight = (thirdheight + 1) // 3
    for i in range(9):
        for j in range(9):
            pygame.draw.rect(DISPLAYSURF, pygame.Color('gray'),
                             pygame.Rect((ninthwidth * i), (ninthheight * j), ninthwidth, ninthheight), 1)


# Displays numbers on board
def shownumbers(board):
    ninthwidth = (DISPLAYWIDTH * 1.02) // 9
    ninthheight = (DISPLAYHEIGHT * 1.01) // 9

    font = pygame.font.SysFont("Arial", 36)
    DISPLAYSURF.fill((255, 255, 255))
    makegrid()

    for i in range(9):
        for j in range(9):
            text = font.render(str(board[j][i]), True, pygame.Color('black'))
            DISPLAYSURF.blit(text, (int(ninthwidth * i), int(ninthheight * j)))
    pygame.display.update()


# Takes click position on the board and gets the exact position of the number in that square in terms of index
def clickposition(origposition):
    if origposition[0] < DISPLAYWIDTH and origposition[1] < DISPLAYHEIGHT:
        remainderx = origposition[0] % ((DISPLAYWIDTH * 1.02) // 9)
        properx = origposition[0] - remainderx
        remaindery = origposition[1] % ((DISPLAYHEIGHT * 1.01) // 9)
        propery = origposition[1] - remaindery

        xindex = properx // ((DISPLAYWIDTH * 1.02) // 9)
        yindex = propery // ((DISPLAYHEIGHT * 1.01) // 9)
        return int(xindex), int(yindex)


# Checks if the finished board is a valid sudoku board or not
def validboard(board):
    for i in range(9):
        for j in range(9):
            ybox = j // 3
            xbox = i // 3
            if check_column(board, j, board[i][j], (i, j)) and check_row(board, i, board[i][j], (i, j)) and \
                    check_box(board, xbox, ybox, board[i][j], (i, j)):
                continue
            else:
                # Board is invalid
                return False
    # Board is valid
    return True


def main():
    global FPSCLOCK, DISPLAYSURF, DISPLAYWIDTH, DISPLAYHEIGHT, FPS
    global gameboard
    board_generator.setmasterboard()
    gameboard = board_generator.getmasterboard()
    FPSCLOCK = pygame.time.Clock()
    FPS = 60
    pygame.init()
    DISPLAYWIDTH = 800
    DISPLAYHEIGHT = 600
    DISPLAYSURF = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))
    pygame.display.set_caption('Sudoku Solver')

    key = None
    selectednumber = None
    fillbooleanboard(gameboard)

    # Main game loop
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # If a key is pressed on the keyboard
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

                # Basically "deleting" a number from the board
                if event.key == pygame.K_BACKSPACE or event.key == pygame.K_DELETE:
                    key = 0

                # Checking that there is an input for the number and it wasn't a number from the start
                if selectednumber is not None and not booleanboard[selectednumber[1]][selectednumber[0]]:
                    gameboard[selectednumber[1]][selectednumber[0]] = key
                else:
                    key = None

                # If the space bar is pressed the game will attempt to solve itself
                if event.key == pygame.K_SPACE:
                    key = None
                    issolvable = simple_solver(gameboard)
                    # If the board is not solvable
                    if issolvable is False:
                        DISPLAYSURF.fill((255, 255, 255))
                        font = pygame.font.SysFont("Arial", 50)
                        text = font.render("Board is not solvable. Keep playing in 5 seconds!", True,
                                           pygame.Color('green'))
                        DISPLAYSURF.blit(text, (int(DISPLAYWIDTH // 6), int(DISPLAYHEIGHT // 4)))
                        pygame.display.update()
                        time.sleep(5)

                # If the user presses the "c" key and the board is full, the board will be checked for a validity
                if event.key == pygame.K_c and find_empty_space(gameboard) is None:
                    print('here')
                    font = pygame.font.SysFont("Arial", 50)
                    isvalid = validboard(gameboard)
                    DISPLAYSURF.fill((255, 255, 255))
                    if isvalid is True:
                        text = font.render("Congratulations! You win! ", True, pygame.Color('red'))
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

            # If the mouse button is pressed, the key is reset to None and the position is found in terms of square
            if event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                selectednumber = clickposition(position)
                key = None

        # On every pass the grid is repainted, the numbers are repainted, the display is updated, and clock ticks FPS
        makegrid()
        shownumbers(gameboard)
        pygame.display.update()
        FPSCLOCK.tick(FPS)


if __name__ == '__main__':
    main()
