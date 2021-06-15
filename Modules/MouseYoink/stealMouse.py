import time

import mouse


def moveMouseTo(pos):
    mouse.move(pos[0], pos[1])


for i in range(10):
    moveMouseTo((i, i))
