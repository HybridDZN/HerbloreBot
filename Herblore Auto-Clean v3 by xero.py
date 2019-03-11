#Herblore Auto-Clean Bot v3 written By xero
#Importing required modules
from pynput.mouse import Button, Controller
import time
#Script
mouse = Controller()
#Column Values
column_1 = 0
column_2 = 0
column_3 = 0
column_4 = 0
#Column 1
mouse.position = (1700,770)
for column_1 in range(7):
    mouse.click(Button.left, 1)
    time.sleep(.04)
    mouse.move(0, 36)
    time.sleep(.04)
    column_1 = column_1 + 1
#Column 2
if column_1 == 7:
    mouse.position = (1736,770)
    for column in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.04)
        mouse.move(0, 36)
        time.sleep(.04)
        column_2 = column_2 + 1
#Column 3
if column_2 == 7:
    mouse.position = (1780,770)
    for column_3 in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.04)
        mouse.move(0, 36)
        time.sleep(.04)
        column_3 = column_3 + 1
#Column 4
if column_3 == 7:
    mouse.position = (1815,770)
    for column_4 in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.04)
        mouse.move(0, 36)
        time.sleep(.04)
        column_4 = column_4 + 1
#Script quit statement    
if column_4 == 7:
    quit()
