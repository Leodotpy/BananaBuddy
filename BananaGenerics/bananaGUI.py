import PySimpleGUI as sg
from PIL import Image

import settings


class BananaVisualizer:
    position = (0.0, 0.0)
    bananaWin = None

    # SETS UP ENTIRE BANANA
    def __init__(self, pos):
        self.DISPLAY_TIME_MILLISECONDS = 0
        self.position = pos
        self.createBananaImage()
        self.createBananaWin(pos)
        # self.FILENAME = ''
        self.showBanana()

    def createBananaImage(self, original_img_dir=r'res/default.png',
                          basewidth=200):  # default values for default banana
        # create resized banana image
        img = Image.open(original_img_dir)  # if you want to use a file instead of data, then use this in Image Element
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        img = img.resize((basewidth, hsize), Image.ANTIALIAS)
        FILENAME = r'tmp/1.png'
        img.save(FILENAME)
        self.FILENAME = FILENAME

    # CREATE BANANA WINDOW ON START
    def createBananaWin(self, pos):
        # set up transparent banana window
        self.bananaWin = sg.Window('Window Title', [[sg.Image(self.FILENAME)]],
                                   transparent_color=sg.theme_background_color(),
                                   no_titlebar=True,
                                   keep_on_top=True, grab_anywhere=False,
                                   location=pos, alpha_channel=1)

    # SHOWS THE BANANA
    def showBanana(self):
        self.bananaWin.read(self.DISPLAY_TIME_MILLISECONDS)

    # GRAPHICS TICK
    # RUNS ON FIXED TIMER IN MAIN, MOVES BANANA TO WHEREVER ITS "MATH" POSITION IS
    def updateWinPos(self):
        self.bananaWin.move(int(self.position[0]), int(self.position[1]))
        self.bananaWin.refresh()

    # PHYSICS TICK
    # UPDATES THE INTERNAL GUI POSITION VARIABLE
    def moveBanana(self, newpos):
        self.position = newpos
