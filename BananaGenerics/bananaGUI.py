class BananaVisualizer:

    position = (0.0, 0.0)

    def __init__(self, pos):
        self.position = pos
        self.createbananawin(pos)


    #CREATE BANANA WINDOW ON START
    def createbananawin(self, pos):



    #RUNS ON FIXED TIMER IN MAIN, MOVES BANANA TO WHEREVER ITS "MATH" POSITION IS
    def updatebananapos(self):


    # UPDATES THE INTERNAL GUI POSITION VARIABLE
    def movebanana(self, newPos):
        self.position = newPos
