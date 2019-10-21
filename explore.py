#!/usr/bin/env python

from robot import *
import random
from time import sleep

distances=[]
try:
    for i in range(80):
        d=get_distance()
        distances.append(d)
        turn_right(0.05)
        sleep(0.2)
    for d in distances:
        print "%.2f" % d

except KeyboardInterrupt:
       print "Cleaning up"
       stop()
       cleanup()
