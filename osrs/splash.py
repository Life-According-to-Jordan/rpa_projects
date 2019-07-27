from pynput.mouse import Button, Controller
import time
import random
from playsound import playsound

mouse = Controller()

#print('The current pointer position is {0}'.format(mouse.position))

mouse.position = (683.9921875, 270.5)

#activate osrs client by clicking on it
print ('*** Hit CTRL+C to stop ***')

mouse.press(Button.left)
mouse.release(Button.left)

time.sleep(3)

i = 0

#set limit for number of iterations
while i < 10000:

    #set random variables for mouse click
    MOUSE_LOWERBOUND = random.uniform(601.01,735.45)
    MOUSE_UPPERBOUND = random.uniform(281.207,440.636)

    #set random location for mouse click
    mouse.position = (MOUSE_LOWERBOUND, MOUSE_UPPERBOUND)

    #iterate through number of alcs
    i += 1

    print(i)
