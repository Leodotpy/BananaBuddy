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

