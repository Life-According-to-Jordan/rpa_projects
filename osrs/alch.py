from pynput.mouse import Button, Controller
import time
import random
from playsound import playsound

mouse = Controller()

#identify current location of mouse
print('The current pointer position is {0}'.format(
    mouse.position))

#initialize mouse location
mouse.position = (2492.18359375, 802.8984375)

#activate osrs client by clicking on it
print ('*** Hit CTRL+C to stop ***')

#used to activate window
#consider removing
mouse.press(Button.left)
mouse.release(Button.left)

#wait for script to start working
time.sleep(1.5)

i = 0

LIMIT = 4000

#set limit for number of iterations
while i < LIMIT:

    #set random variables for mouse click
    MOUSE_LOWERBOUND = random.uniform(2492.01,2497.45)
    MOUSE_UPPERBOUND = random.uniform(808.84375,811.84375)

    #set random location for mouse click
    mouse.position = (MOUSE_LOWERBOUND, MOUSE_UPPERBOUND)

    #iterate through number of alcs
    i += 1

    #click high alc
    mouse.press(Button.left)
    time.sleep(random.uniform(0.1,0.2))
    mouse.release(Button.left)
    time.sleep(random.uniform(2.5,2.7))

    #click item to alc
    mouse.press(Button.left)
    time.sleep(random.uniform(0.1,0.2))
    mouse.release(Button.left)
    time.sleep(random.uniform(1,1.2))

    #number of high alcs performed
    print(i)

    #add in short breaks every few hundred alcs
    if i in [813, 1546, 1702, 2444, 3284, 3518, 4206, 4784, 5461, 6142, 6789, 7342, 7935, 9001]:
        print('bathroom break')
        time.sleep(random.randint(1,13))

    #add in medium breaks every few thousand alcs
    if i in [2713, 4351, 6521, 8673]:
        print('bathroom break')
        time.sleep(60)

    #set alarm for when code is close to finishing iteration limit
    while i > LIMIT - 5:
        playsound('hey.wav')
        playsound('listen.wav')
