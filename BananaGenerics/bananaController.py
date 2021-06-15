import settings
from BananaGenerics.bananaGUI import BananaVisualizer
import numpy


class Banana:

    speed = [0.0, 0.0]
    position = [0.0, 0.0]
    bananaWin = None


    def __init__(self, pos):
        self.position = pos
        self.bananaWin = BananaVisualizer(self.position)

    def bananastep(self, desiredPos, deltaTime):
        self.bananawalkx(desiredPos[0], deltaTime)

        self.position[0] += self.speed[0]
        self.position[1] += self.speed[1]

        self.bananaWin.moveBanana(newpos=self.position)

        # UPDATE POSITION VECTOR

        #TEMP
        self.bananaWin.updateWinPos()

    def bananawalkx(self, desiredX, deltaTime):
        diff = desiredX - self.position[0]
        if diff != 0:
            accelerationAmnt = (diff / abs(diff)) * deltaTime
        else:
            accelerationAmnt = 0

        self.speed[0] += accelerationAmnt * settings.accelerationRate

        if self.position[0] < 0:
            self.position[0] = 0
            self.speed[0] = abs(self.speed[0])

        if self.position[0] > settings.screen_res[0]:
            self.position[0] = settings.screen_res[0]
            self.speed[0] = -abs(self.speed[0])
