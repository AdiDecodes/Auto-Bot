######################################################################################################
""" LIBRARIES """

import time, random, sys
import pandas as pd
import numpy as np

import pynput.mouse as mouse
import pynput.keyboard as keyboard
import pyperclip, pyautogui, pytesseract, cv2

from PIL import Image
from datetime import datetime

mouse_button = mouse.Button
mouse = mouse.Controller()

keyboard_key = keyboard.Key
keyboard = keyboard.Controller()

######################################################################################################
""" MAC VARIABLES """

# pointer coordinates
# BALANCE = (1090, 145)
# INPUT = (1150, 220)
# BUY = (1180, 500)
# SELL = (1180, 560)
# BLANK = (1180, 650)
# REFRESH = (1057, 76)

# # screenshot regions
# SS_RSI = (2010, 1140, 100, 100)
# SS_STOCHASTIC = (2010, 1300, 100, 100)
# SS_PRICE = (1855, 550, 300, 400)
# SS_EARNINGS = (1345, 350, 300, 100)

# # screenshot paths
# PATH_RSI = 'Binary/binomo/ss/rsi.png'
# PATH_STOCHASTIC = 'Binary/binomo/ss/stochastic.png'
# PATH_PRICE = 'Binary/binomo/ss/price.png'
# PATH_EARNINGS = 'Binary/binomo/ss/earnings.png'
# PATH_TEST = 'Binary/binomo/ss/test.png'

# # utility paths
# PATH_CSV = 'Binary/binomo/data.csv'
# pytesseract.pytesseract.tesseract_cmd = 'Users/Admin/AppData/Local/Programs/Python/Python39/Scripts/pytesseract'
# copy_button = keyboard_key.cmd

######################################################################################################
""" WINDOWS VARIABLES """

# pointer coordinates
BALANCE = (1717, 114)
INPUT = (1235, 195)
BUY = (1820, 475)
SELL = (1820, 536)
BLANK = (1480, 100)
REFRESH = (1047, 52)
PLUS = (1883, 240)
MINUS = (1883, 263)
TIME = (1777, 260)
TIME_BOX = (1823, 250)
TIME_SELECT = (1644, 422)

# screenshot regions
SS_RSI = (1090, 570, 50, 50)
SS_STOCHASTIC = (1090, 650, 50, 50)
SS_PRICE = (960, 240, 200, 300)
SS_EARNINGS = (620, 150, 140, 50)

# screenshot paths
PATH_RSI = 'ss\\rsi.png'
PATH_STOCHASTIC = 'ss\\stochastic.png'
PATH_PRICE = 'ss\\price.png'
PATH_EARNINGS = 'ss\\earnings.png'
PATH_TEST = 'ss\\test.png'

# utility paths
PATH_CSV = 'data.csv'
pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\\tesseract.exe'
copy_button = keyboard_key.ctrl

# uncomment

# MAC:
# copy_button = keyboard_key.cmd

# WINDOWS:
# copy_button = keyboard_key.ctrl

# POP_UP = (1099, 120) - WINDOWS