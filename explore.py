#!/usr/bin/env python

from robot import *
import random
from time import sleep

distances = [] # An empty list
voids = []

threshold = 100
void = 1500

# Battery? 0.05 - Power 0.1
turn_time = 0.05

def check_void(counter, start_void):
    if counter>0:
        print "void size is", counter
        voids.append((start_void, counter))

def scan():
    for i in range(30):
        d=get_distance()
        if d>=threshold:
            d=void
        distances.append(d)
        turn_right(turn_time)
        sleep(0.2)

def do_voids():
    i = 0
    counter = 0
    start_void = 0
    for d in distances:
        print "%.2f" % d
        if d==void:
            if counter == 0:
                # Beginning of void
                start_void = i

            counter+=1
        else:
            check_void(counter, start_void)
            counter=0
        i += 1

    check_void(counter, start_void)


try:
    scan()
    do_voids()

    for start, size in voids:
        print "Void starting at ", start, " size ", size

except KeyboardInterrupt:
       print "Cleaning up"
       stop()
       cleanup()
