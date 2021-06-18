import random

import PySimpleGUI as sg
from PIL import Image
import cv2
import settings

# get random banner image
FILENAME = r'Imgs\banana-creampie.jpg'
img = cv2.imread(FILENAME, cv2.IMREAD_UNCHANGED)
imgbytes = cv2.imencode('.png', img)[1].tobytes()

#get image dimentions
img_height, img_width, _ = img.shape

startpos = 0, random.randint(0, settings.screen_res[1])

# setup banner window
DISPLAY_TIME_MILLISECONDS = 0
layout = [[sg.Image(data=imgbytes, key='-POSTER-')]]

banner = sg.Window('Window Title', layout=layout,
                   transparent_color=sg.theme_background_color(),
                   no_titlebar=True,
                   keep_on_top=True, grab_anywhere=False,
                   location=startpos, alpha_channel=1)

banner.read(DISPLAY_TIME_MILLISECONDS)

# slide out animation
for i in range(img_width, 0, -1):
    banner.move(startpos[0] - i, startpos[1])
    banner.refresh()
