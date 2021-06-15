import PySimpleGUI as sg
from PIL import Image

spawnPointX, spawnPointY = 100,100

FILENAME = r'Modules/Banners/Imgs/banana-chips.jpg'
img = Image.open(FILENAME)

# set up transparent banana window
DISPLAY_TIME_MILLISECONDS = 0
banner = sg.Window('Window Title', [[sg.Image(img)]], transparent_color=sg.theme_background_color(),
                   no_titlebar=True,
                   keep_on_top=True, grab_anywhere=False,
                   location=(spawnPointX, spawnPointY), alpha_channel=1)

banner.read(DISPLAY_TIME_MILLISECONDS)
