#Herblore Auto-Clean Bot v2 written By xero
from pynput.mouse import Button, Controller
import time
mouse = Controller()
#Column Values
grimy_column_1 = 0
grimy_column_2 = 0
grimy_column_3 = 0
grimy_column_4 = 0
#Column 1
mouse.position = (1700,770)
for grimy_column_1 in range(7):
    mouse.click(Button.left, 1)
    time.sleep(.1)
    mouse.move(0, 36)
    time.sleep(.1)
    grimy_column_1 = grimy_column_1 + 1
#Column 2
if grimy_column_1 == 7:
    mouse.position = (1736,770)
    for grimy_column in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.1)
        mouse.move(0, 36)
        time.sleep(.1)
        grimy_column_2 = grimy_column_2 + 1
#Column 3
if grimy_column_2 == 7:
    mouse.position = (1779,770)
    for grimy_column_3 in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.1)
        mouse.move(0, 36)
        time.sleep(.1)
        grimy_column_3 = grimy_column_3 + 1
#Column 4
if grimy_column_3 == 7:
    mouse.position = (1813,770)
    for grimy_column_4 in range(7):
        mouse.click(Button.left, 1)
        time.sleep(.1)
        mouse.move(0, 36)
        time.sleep(.1)
        grimy_column_4 = grimy_column_4 + 1
#Script quit statement    
elif grimy_column_4 == 7:
    quit()
