import random
import time

import numpy as np
from PIL import Image

import PySimpleGUI as sg
import pyautogui
import pyautogui as pag
import mouse
import keyboard

import BananaGenerics.bananaController

start_time = time.time()

screenWidth, screenHeight = pag.size()

# create resized banana image
basewidth = 400
img = Image.open(r'res/default.png')  # if you want to use a file instead of data, then use this in Image Element
wpercent = (basewidth / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((basewidth, hsize), Image.ANTIALIAS)
FILENAME = r'tmp/1.png'
img.save(FILENAME)


# set up transparent banana window
DISPLAY_TIME_MILLISECONDS = 0
startX, startY = int(screenWidth / 2), int(screenHeight / 2)
banana = sg.Window('Window Title', [[sg.Image(FILENAME)]], transparent_color=sg.theme_background_color(),
                   no_titlebar=True,
                   keep_on_top=True, grab_anywhere=False,
                   location=(startX, startY), alpha_channel=1)

banana.read(DISPLAY_TIME_MILLISECONDS)

# incase the banana gets out of hand,
def forceExit():
    print("Force Close")
    banana.Close()
    exit()
keyboard.add_hotkey("ctrl + k", forceExit)


speedmultiplier = 20
banana_offset = 100

banana = BananaGenerics.bananaController.Banana()

# main loop

while True:
    bananaX, bananaY = banana.current_location()[0] -1, banana.current_location()[1] -2
    mouseX, mouseY = mouse.get_position()

    dx, dy = (bananaX - mouseX, bananaY - mouseY)
    stepx, stepy = (dx / (40. * speedmultiplier) , dy / (20.*speedmultiplier))

    banana.move(bananaX - int(stepx * 2), bananaY - int(stepy * 2))
    print(banana.current_location())

    banana.refresh()

