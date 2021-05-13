import pyautogui as pg
import time
import cv2
import numpy as np
from image_slicer import slice
from PIL import Image
from pytesseract import *
pytesseract.tesseract_cmd = r'C:\Users\jakub\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'


def converter(img):
    img = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_OTSU)
    print ("Threshold selected : ", ret)
    cv2.imwrite("./output_image.png", thresh)


    num9 = Image.open('output_image.png')
    new_size = tuple(2*x for x in num9.size)
    num9 = num9.resize(new_size, Image.ANTIALIAS)
    num9cr = num9.crop((21, 25, 110, 110))
    num9t = pytesseract.image_to_string(num9cr, lang='eng', config='--psm 6')
    if num9t.find('Gg')!= -1:
        num9t = str(9)
    if num9t.find('g') != -1:
        num9t = str(9)
    return num9t

