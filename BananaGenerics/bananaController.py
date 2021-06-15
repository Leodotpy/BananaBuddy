import settings
import math


class Banana:
    speed = [0.0, 0.0]
    position = [0.0, 0.0]

    # def __init__(self):

    def bananastep(self, desiredPos, deltaTime):
        self.bananawalkx(desiredPos[0], deltaTime)

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
