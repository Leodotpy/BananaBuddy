import PySimpleGUI as sg
import cv2
from PIL import Image, ImageOps

import settings
import io

class BananaVisualizer:
    position = (0.0, 0.0)
    bananaWin = None

    # SETS UP ENTIRE BANANA
    def __init__(self, pos):
        self.DISPLAY_TIME_MILLISECONDS = 0
        self.position = pos
        self.direction_file = ''
        self.direction = ''

        self.createBananaImages()
        self.createBananaWin(pos)
        # self.FILENAME = ''
        self.showBanana()

    def createBananaImages(self, original_img_dir=r'res/default.png',
                           basewidth=200):  # default values for default banana

        # create resized right facing banana image
        img = Image.open(original_img_dir)  # if you want to use a file instead of data, then use this in Image Element
        wpercent = (basewidth / float(img.size[0]))
        hsize = int((float(img.size[1]) * float(wpercent)))
        right = img.resize((basewidth, hsize), Image.ANTIALIAS)

        self.direction = 'right'
        self.direction_file = 'tmp/' + str(self.direction) + '.png'
        right.save(self.direction_file)

        # flip right image to create one facing left
        self.direction = 'left'
        self.direction_file = 'tmp/' + str(self.direction) + '.png'
        left = ImageOps.mirror(right)
        left.save(self.direction_file)

        self.direction_file = self.direction_file

    # CREATE BANANA WINDOW ON START
    def createBananaWin(self, pos):
        # set up transparent banana window

        layout = [[sg.Image(self.direction_file, key='-IMAGE-')]]

        self.bananaWin = sg.Window('Window Title', layout=layout,
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

    def setBananaFacingDirection(self, direction):
        self.direction = direction

        self.direction_file = 'tmp/' + str(self.direction) + '.png'

        img = cv2.imread(self.direction_file, cv2.IMREAD_UNCHANGED)
        imgbytes = cv2.imencode('.png', img)[1].tobytes()

        self.bananaWin['-IMAGE-'].update(data=imgbytes)
        self.bananaWin.refresh()
