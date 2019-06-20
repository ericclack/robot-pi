#!/usr/bin/env python

from robot import *
import random
from time import sleep

# Move about and avoid collisions

try:
    while True:
        forwards(0.05)
	sleep(0.05)

        d=get_distance()
        if d < 25 :
            #we want to turn one way or the other
            turn=random.choice([turn_left,turn_right])
            while d < 25:
                turn(0.1)
                sleep(0.2)
                d=get_distance()

except KeyboardInterrupt:
       print "Cleaning up"
       stop()
       cleanup()
