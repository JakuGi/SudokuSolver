import pyautogui as pg
import time
import cv2
import numpy as np
from image_slicer import slice
import tester
import solver
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\jakub\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'



class locater():
    def main(self):
        self.sudoku = self.boardFinder()
        if self.sudoku is not None:
            self.squares = self.square()
            self.img = cv2.imread('images/sudokubrd_cap.png')
            self.grayimg = self.canny()
            self.cpImg = self.canny.copy()
            self.colorConvImg = cv2.cvtColor(self.img, cv2.COLOR_RGB2BGR)
            cv2.imwrite('images/sudokubrd_canny.png', self.grayimg)
            slice('images/sudokubrd_canny.png', 9*9,)
            self.numlist = self.numDetector()
            solver.solver(self.numlist)
            # plt.imshow(self.canny)
            # plt.show()
            # cv2.imshow('br', self.grayimg)
            # cv2.waitKey(0)

    def canny(self):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_RGB2GRAY)
        self.blur = cv2.GaussianBlur(self.gray, (5,5),0)
        self.canny = cv2.Canny(self.blur, 150, 920)
        return self.blur


    def boardFinder(self):
        time.sleep(0.5)
        self.sudoku = pg.locateOnScreen('images/boardtest.PNG', confidence=0.6)
        print(self.sudoku)
        self.sudoku_b = pg.screenshot(region=self.sudoku)
        self.sudoku_b.save('images/sudokubrd_cap.png')
        return self.sudoku
    
    
    def square(self):
        self.squares = []
        checker = False
        z=0
        for col in range(9):
            if checker:
                z+= 55
            x, y = 0, 55
            checker = True
            for row in range(9):
                x += 55
                y += 55
                self.squares.append([(z, x), (y, y)])
        click_coo = self.squares[10][1]
        # pg.click(click_coo[0] + self.sudoku.left, click_coo[1] + self.sudoku.top)
        return self.squares

    def numDetector(self):
        self.numlist = []
        self.final_list = []
        y = 0
        for col in range(9):
            print('col' + str(y))
            x = 1
            if y >= 1:
                self.final_list.append(self.numlist)
                self.numlist = []
            y += 1
            for row in range(9):
                print('row'+str(x))
                self.compimg = cv2.imread('images/sudokubrd_canny_0' + str(y) + '_0' + str(x) + '.png')
                self.detNum = tester.converter(self.compimg)
                if self.detNum.find(str(1)) is not -1:
                    self.numlist.append(1)
                elif self.detNum.find(str(2)) is not -1:
                    self.numlist.append(2)
                elif self.detNum.find(str(3)) is not -1:
                    self.numlist.append(3)
                elif self.detNum.find(str(4)) is not -1:
                    self.numlist.append(4)
                elif self.detNum.find(str(5)) is not -1:
                    self.numlist.append(5)
                elif self.detNum.find(str(6)) is not -1:
                    self.numlist.append(6)
                elif self.detNum.find(str(7)) is not -1:
                    self.numlist.append(7)
                elif self.detNum.find(str(8)) is not -1:
                    self.numlist.append(8)
                elif self.detNum.find(str(9)) is not -1:
                    self.numlist.append(9)
                else:
                    self.numlist.append(0)
                
        
                x+=1
        
        self.final_list.append(self.numlist)
        print(self.final_list)
        return self.final_list



if __name__ == '__main__':
    app = locater()
    start_time = time.time()
    app.main()
    print("--- %s seconds ---" % (time.time() - start_time))

