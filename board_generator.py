import random
import visual_sudoku
global masterBoard


def getmasterboard():
    return masterBoard


def setmasterboard():
    global masterBoard
    masterBoard = []
    for i in range(9):
        rowlist = []

        for j in range(9):
            randnumber = random.randint(0, 9)
            if randnumber not in rowlist:
                rowlist.append(randnumber)
            else:
                rowlist.append(0)

        masterBoard.append(rowlist)

    for i in range(9):
        for j in range(9):
            boxcheck = visual_sudoku.check_box(getmasterboard(), i // 3, j // 3, masterBoard[i][j], (i, j))
            if boxcheck is False:
                getmasterboard()[i][j] = 0
            columncheck = visual_sudoku.check_column(getmasterboard(), j, getmasterboard()[i][j], (i, j))
            if columncheck is False:
                getmasterboard()[i][j] = 0
