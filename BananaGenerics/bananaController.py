import settings
from BananaGenerics.bananaGUI import BananaVisualizer
import numpy


class Banana:
    speed = [0.0, 0.0]
    position = [0.0, 0.0]
    size = [0.0, 0.0]
    bananaWin = None

    def __init__(self, pos, basewidth):
        self.position = pos
        self.bananaWin = BananaVisualizer(self.position)
        self.size = self.bananaWin.bananaWin.size

    def bananastep(self, desiredPos, deltaTime):
        desiredPos[0] -= self.size[0]/2
        self.bananawalkx(desiredPos[0], deltaTime)

        self.position[0] += self.speed[0] * deltaTime
        self.position[1] += self.speed[1] * deltaTime

        self.speed[0] /= ((settings.dragCoefficient - 1) * deltaTime) + 1

        if abs(self.speed[0]) < settings.smallestStoppingSpeed and abs(desiredPos[0] - self.position[0]) < settings.smallestStoppingDistance:
            self.speed[0] = 0
            self.position[0] = desiredPos[0]

        self.bananaWin.moveBanana(newpos=self.position)

        # UPDATE POSITION VECTOR

        # TEMP
        self.bananaWin.updateWinPos()

    def bananawalkx(self, desiredX, deltaTime):
        diff = desiredX - self.position[0]
        if diff != 0:
            accelerationAmnt = (diff / abs(diff))
        else:
            accelerationAmnt = 0

        self.speed[0] += accelerationAmnt * settings.accelerationRate * deltaTime * self.brakingcalculation(desiredX)

        if self.position[0] < 0:
            self.position[0] = 0
            self.speed[0] = abs(self.speed[0])

        if self.position[0] > settings.screen_res[0] - self.size[0]:
            self.position[0] = settings.screen_res[0] - self.size[0]
            self.speed[0] = -abs(self.speed[0])

    # PHYSICS CALC TO DETERMINE WHEN TO BRAKE
    def brakingcalculation(self, desiredPosX):
        if desiredPosX == self.position[0]:
            return 0
        reqAcc = (self.speed[0] * abs(self.speed[0])) / (2 * (desiredPosX - self.position[0]))
        if reqAcc > settings.accelerationRate:
            return -1
        return 1
