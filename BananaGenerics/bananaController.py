import settings
import math

class Banana:

    speed = (0.0, 0.0)
    position = (0.0, 0.0)

    def __init__(self):


    def bananastep(desiredPos):
        desiredPos.bananawalkx(desiredPos[0])

    def bananawalkx(self, desiredX):
        diff = desiredX - self.position[0]
        accelerationAmnt = diff / abs(diff)
        self.speed[0] += accelerationAmnt*settings.accelerationRate

        #if self.position[0] < 0:
            #self.position[0] = (0, self.position[1])
            #self.speed[0] = abs(self.speed[0])

        #if self.position[0] < 0:
            #self.position[0] = 0
            #self.speed[0] = abs(self.speed[0])
