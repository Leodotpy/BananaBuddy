import random
import time

import numpy as np
from PIL import Image

import PySimpleGUI as sg
import pyautogui
import pyautogui as pag
import mouse
import keyboard

import BananaGenerics.bananaController as bCON
import settings

start_time = time.time()

screenWidth, screenHeight = pag.size()


# incase the banana gets out of hand,
def forceExit():
    print("Force Close")
    banana.bananaWin.Close()
    exit()


keyboard.add_hotkey("ctrl + k", forceExit)

speedmultiplier = 20
banana_offset = 100

# main loop

banana = bCON.Banana(pos=[100, pag.size()[1] - 200], basewidth=200)

lastTime = time.time_ns()

banana.bananaWin.setBananaFacingDirection('right')
print(banana.bananaWin.direction)
while True:
    currentTime = time.time_ns()
    deltaTime = (currentTime - lastTime) / settings.nano_const
    lastTime = time.time_ns()
    banana.bananastep(list(mouse.get_position()), deltaTime)

