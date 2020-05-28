import random
import sudoku
global masterBoard


# Gets the board that is generated
def getmasterboard():
    return masterBoard


# Sets the board that will be generated
def setmasterboard():
    global masterBoard
    masterBoard = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    # Makes the first row random to better randomize values for the board
    for i in range(9):
        randint = random.randint(1, 9)
        if sudoku.check_row(getmasterboard(), 0, randint, (0, i)) is True:
            masterBoard[0][i] = randint

    # Solve the board to then make a board that is valid
    sudoku.simple_solver(getmasterboard())

    # Randomly take places away from the board
    for i in range(random.randint(35, 64)):
        randx = random.randint(0, 8)
        randy = random.randint(0, 8)
        masterBoard[randx][randy] = 0
