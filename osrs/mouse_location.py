from pynput.mouse import Button, Controller
import time
import random
from playsound import playsound

mouse = Controller()

time.sleep(3)

while True:
    print('The current pointer position is {0}'.format(mouse.position))
    time.sleep(1)
