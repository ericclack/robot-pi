#!/usr/bin/env python

from robot import *
import random
from time import sleep

distances = [] # An empty list
threshold = 100
void = 1500
counter = 0

# Battery? 0.05 - Power 0.1
turn_time = 0.09

def check_void(counter):
    if counter>0:
        print "void size is", counter

try:
    for i in range(30):
        d=get_distance()
        if d>=threshold:
            d=void
        distances.append(d)
        turn_right(turn_time)
        sleep(0.2)
    for d in distances:
        print "%.2f" % d
        if d==void:
            counter+=1
        else:
            check_void(counter)
            counter=0
    check_void(counter)


except KeyboardInterrupt:
       print "Cleaning up"
       stop()
       cleanup()
