import pyautogui as pag
from win32api import GetMonitorInfo, MonitorFromPoint

# CONSTANTS
nano_const = pow(10, 9)

# PHYSICS
accelerationRate = 800
dragCoefficient = 1.02
smallestStoppingSpeed = 1
smallestStoppingDistance = 1

# Get all nessesary monitor dimention information
monitor_info = GetMonitorInfo(MonitorFromPoint((0, 0)))
raw_work_area = monitor_info.get("Work")
raw_monitor_area = monitor_info.get("Monitor")

monitor_area = raw_monitor_area[2], raw_monitor_area[3]
print("The monitor size is {}x{}.".format(monitor_area[0], monitor_area[1]))

taskbar_height = raw_monitor_area[3] - raw_work_area[3]
print("The taskbar height is {}.".format(taskbar_height))

work_area = [raw_work_area[2], raw_work_area[3]]
print("The work area size is {}x{}.".format(work_area[0], work_area[1]))
