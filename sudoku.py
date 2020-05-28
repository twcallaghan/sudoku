# This same code is copied in visual_sudoku. This can solve the sudoku board with basic text and has no graphics
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


def print_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + + + +")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")


# Finds the next empty space in the board (rows before cols)
def find_empty_space(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j


# Checks the column to see if the number attempting to be inserted is already there
def check_column(board, col, num, ignorepos):
    for i in range(len(board)):
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

    if emptyspace is None:
        return True

    for i in range(1, 10):
        ybox = emptyspace[1] // 3
        xbox = emptyspace[0] // 3
        if check_column(board, emptyspace[1], i, None) and check_row(board, emptyspace[0], i, None) and \
                check_box(board, xbox, ybox, i, None):
            board[emptyspace[0]][emptyspace[1]] = i
            if simple_solver(board):
                return True
            board[emptyspace[0]][emptyspace[1]] = 0
    return False


if __name__ == '__main__':
    print_board(gameBoard)
    print("\n")
    if simple_solver(gameBoard):
        print_board(gameBoard)
    else:
        print("No solution")
