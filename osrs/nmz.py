from pynput.mouse import Button, Controller
import time
import random
from playsound import playsound

mouse = Controller()

#print('The current pointer position is {0}'.format(mouse.position))

#activate osrs client by clicking on it
print ('*** Hit CTRL+C to stop ***')

i = 0


#set limit for number of iterations
while i < 10000:

    #set random variables for mouse click
    MOUSE_LOWERBOUND = random.uniform(3590.15,3590.39)
    MOUSE_UPPERBOUND = random.uniform(496.96,497.2)

    #set random location for mouse click
    mouse.position = (MOUSE_LOWERBOUND, MOUSE_UPPERBOUND)

    #iterate through number of alcs
    i += 1

    mouse.press(Button.left)
    time.sleep(random.uniform(0.05,0.1))
    mouse.release(Button.left)

    mouse.press(Button.left)
    time.sleep(random.uniform(0.05,0.1))
    mouse.release(Button.left)

    time.sleep(random.uniform(45,55))

    print(i)
