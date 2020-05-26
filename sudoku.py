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
                print(" | ", end = "")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end = "")

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

    visual_sudoku.showNumbers(board)

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


if __name__ == '__main__':
    print_board(gameBoard)
    print("\n")
    if simple_solver(gameBoard):
        print_board(gameBoard)
    else:
        print("No solution")