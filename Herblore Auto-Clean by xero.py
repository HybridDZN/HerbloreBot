#Herblore Auto-Clean Bot v1 written By xero
from pynput.mouse import Button, Controller
import time

mouse = Controller()
#Setting the initial mouse position
mouse.position = (1700,770)
#column Value
clean_column = 0
herb_number = 0
#First column
while (clean_column < 28):
    mouse.click(Button.left, 1)
    time.sleep(.3)
    mouse.move(0, 36)
    time.sleep(.3)
    clean_column = clean_column + 1
    herb_number = herb_number + 1
    #Checking for column completion
if (herb_number == 7):
    mouse.move(36, -258)
    herb_number = 1
#Script quit statement    
elif (clean_column == 28):
    quit()

print('Out of loop')

#Check for mouse position
#mouse._position_get
#print(mouse.position)