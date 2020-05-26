gameBoard = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
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
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j

def simple_solver(board):
    emptyspace = find_empty_space(board)
    while emptyspace is not None:
        rowcolvalues = []
        for i in range(0, 9):
            if board[emptyspace[0]][i] not in rowcolvalues:
                rowcolvalues.append(board[emptyspace[0]][i])
            if board[i][emptyspace[1]] not in rowcolvalues:
                rowcolvalues.append(board[i][emptyspace[1]])

        xbox = emptyspace[0] // 3
        ybox = emptyspace[1] // 3

        for i in range(xbox, xbox + 3):
            for j in range(ybox, ybox + 3):
                if board[i][j] not in rowcolvalues:
                    rowcolvalues.append(board[i][j])

        rowcolvalues = sorted(rowcolvalues)

        for i in range(1, 10):
            if i not in rowcolvalues:
                board[emptyspace[0]][emptyspace[1]] = i
                break

        emptyspace = find_empty_space(board)
        print_board(board)
        print("\n")

if __name__ == '__main__':
    print_board(gameBoard)
    print(simple_solver(gameBoard))
    #print_board(gameBoard)