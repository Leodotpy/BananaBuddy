import pyautogui as pag

# CONSTANTS
nano_const = pow(10, 9)

# PHYSICS
gravity = -4000.0
accelerationRate = 800
dragCoefficient = 1.02
smallestStoppingSpeed = 1
smallestStoppingDistance = 1

# CHARACTER MOVING
jumpSpeedRetentions = (2, 1, 0)
jumpHeights = (0.1, 0.5, 1.0)



screen_res = pag.size()
