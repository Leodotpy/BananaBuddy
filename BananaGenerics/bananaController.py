import math

import numpy

import settings
from BananaGenerics.bananaGUI import BananaVisualizer


class Banana:
    speed = [0.0, 0.0]
    position = [0.0, 0.0]
    size = [0.0, 0.0]
    bananaWin = None
    grounded = False

    def __init__(self, pos, basewidth):
        self.grounded = False
        self.position = pos
        self.bananaWin = BananaVisualizer(self.position)
        self.size = self.bananaWin.bananaWin.size

    def bananastep(self, desiredPos, deltaTime):
        desiredPos[0] -= self.size[0] / 2
        desiredPos[1] = settings.screen_res[1] - desiredPos[1]

        # -- MOVEMENT --
        if self.grounded:
            # walk and apply drag when grounded
            self.bananawalkx(desiredPos[0], deltaTime)
            self.speed[0] /= ((settings.dragCoefficient - 1) * deltaTime) + 1
            # attempt jumps
            if self.grounded:
                self.jumpingCalculation(desiredPos)
        else:
            # apply gravity when not grounded
            self.speed[1] += settings.gravity * deltaTime

        self.position[0] += self.speed[0] * deltaTime
        self.position[1] += self.speed[1] * deltaTime

        # stop horizontal movement when player is close enough
        if abs(self.speed[0]) < settings.smallestStoppingSpeed and abs(
                desiredPos[0] - self.position[0]) < settings.smallestStoppingDistance:
            self.speed[0] = 0
            self.position[0] = desiredPos[0]

        self.wallcontainer()
        self.bananaWin.moveBanana(newpos=self.position)

        # UPDATE POSITION VECTOR

        # TEMP
        self.bananaWin.updateWinPos()

    def wallcontainer(self):
        if self.position[0] < 0:
            self.position[0] = 0
            self.speed[0] = abs(self.speed[0])

        if self.position[0] > settings.screen_res[0] - self.size[0]:
            self.position[0] = settings.screen_res[0] - self.size[0]
            self.speed[0] = -abs(self.speed[0])

        if self.position[1] < 0:
            self.position[1] = 0
            self.speed[1] = 0
            self.grounded = True

        if self.position[1] > settings.screen_res[1] - self.size[1]:
            self.position[1] = settings.screen_res[1] - self.size[1]
            # self.speed[1] = -abs(self.speed[1])

    def bananawalkx(self, desiredX, deltaTime):
        diff = desiredX - self.position[0]
        if diff != 0:
            accelerationAmnt = (diff / abs(diff))
        else:
            accelerationAmnt = 0

        self.speed[0] += accelerationAmnt * settings.accelerationRate * deltaTime * self.brakingcalculation(desiredX)

    # PHYSICS CALC TO DETERMINE WHEN TO BRAKE
    def brakingcalculation(self, desiredPosX):
        if desiredPosX == self.position[0]:
            return 0
        reqAcc = (self.speed[0] * abs(self.speed[0])) / (2 * (desiredPosX - self.position[0]))
        if reqAcc > settings.accelerationRate:
            return -1
        return 1

    # CALCULATE WHETHER A JUMP WILL TOUCH THE MOUSE OR NOT
    def jumpingCalculation(self, desiredPos):
        xdiff = desiredPos[0] - self.position[0]
        # if stationary, perform perfectly vertical jump
        if self.speed[0] == 0:
            self.speed[1] = math.sqrt(desiredPos[1] * -2.0 * settings.gravity)
            self.grounded = False
            return
        else:
            jumpTime = xdiff / self.speed[0]
            # negative time doesn't work
            if jumpTime < 0:
                return

            # calculate parabolic path
            attemptedYSpeed = desiredPos[1]/jumpTime + 0.5*settings.gravity*jumpTime

            # calculate initial vertical speed upon jump based on desired height
            maxYSpeed = math.sqrt((settings.screen_res[1] - self.size[1]) * -2.0 * settings.gravity)

            if attemptedYSpeed > maxYSpeed:
                return

            self.speed[1] = attemptedYSpeed
            self.grounded = False
