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
import BananaGenerics.bananaGUI as bGUI

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

controller = bCON.Banana()

# main loop

banana = bGUI.BananaVisualizer(pos=(100, 100))

banana.createBananaImage()

banana.spawnBanana()

i = 0
while True:
    banana.moveBanana((500 + i, 500 + i))
    i += 1
