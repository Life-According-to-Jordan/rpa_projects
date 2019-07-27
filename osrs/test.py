import time
import random
from playsound import playsound

i = 0

LIMIT = int(input("Set limit on actions: ")) + 1

#set limit for number of iterations
while i < LIMIT:

    #iterate through number of alcs
    i += 1

    #number of high alcs performed
    print(i)
    time.sleep(1)


    #set alarm for when code is close to finishing iteration limit
    if i > LIMIT - 1:
        print('close to end')
