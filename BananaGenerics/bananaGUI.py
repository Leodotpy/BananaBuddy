import PySimpleGUI as sg
from PIL import Image


class BananaVisualizer:
    position = (0.0, 0.0)
    bananaWin = None

    def __init__(self, pos):
        self.DISPLAY_TIME_MILLISECONDS = 0
        self.position = pos
        self.createBananaImage()
        self.createBananaWin(pos)
        #self.FILENAME = ''


    def createBananaImage(self, original_img_dir=r'res/default.png', basewidth=400):
        # create resized banana image
        banana_width = 400
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

    def spawnBanana(self):
        self.bananaWin.read(self.DISPLAY_TIME_MILLISECONDS)

    # RUNS ON FIXED TIMER IN MAIN, MOVES BANANA TO WHEREVER ITS "MATH" POSITION IS
    def updateBananaPos(self):
        pass

    # UPDATES THE INTERNAL GUI POSITION VARIABLE
    def moveBanana(self, newpos):
        self.bananaWin.move(newpos[0], newpos[1])
        self.bananaWin.refresh()
