import pyautogui as pg
import time
import cv2
import numpy as np
from sudoku import Sudoku
def solver(board):
    # boardInp = input('Board:')
    # boardInp = int(boardInp)
    # boardInpList = []
    # board = []
    # permBoard = []
    # k = 0
    # while boardInp > 0:
    #     boardInpList.append(boardInp % 10)
    #     boardInp = (boardInp - boardInp % 10) // 10
    # boardInpList.reverse()
    # for num in boardInpList:
    #     k+=1
    #     permBoard.append(num)
    #     if k % 9 == 0:
    #         board.append(permBoard)
    #         permBoard =[]
            
    # print(board)
    puzzle = Sudoku(3, 3, board=board)
    print(puzzle)
    puzzleS = puzzle.solve()
    print(puzzleS)
    time.sleep(2)
    print(puzzleS.board)
    checker = False
    for row in puzzleS.board:
        if checker:
            pg.press('down')
            for i in range(10):
                pg.press('left')

        checker = True
        for num in row:
            pg.press('num' + str(num))
            pg.press('right')
