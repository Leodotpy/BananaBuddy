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

# main loop

banana = bCON.Banana(pos=[100, 100])

while True:
    banana.bananastep(mouse.get_position(), 0.1)
