#!/usr/bin/env python

"""Scan environment and move towards biggest void"""

from robot import *
import random
from time import sleep

distances = [] # An empty list
voids = []

threshold = 200
object_stop = 25
void = 1500

# Battery? 0.05 - Power 0.1
turn_time = 0.035
steps=30

def check_void(counter, start_void):
    if counter>0:
        voids.append((start_void, counter))

def clear_lists():
    global distances, voids
    distances = []
    voids = []

def scan():
    clear_lists()
    for i in range(steps):
        d=get_distance()
        if d>=threshold:
            d=void
        distances.append(d)
        turn_right(turn_time)
        sleep(0.2)
    print distances

def do_voids():
    i = 0
    counter = 0
    start_void = 0
    for d in distances:
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

def biggest_void():
    max_size=0
    max_start=0
    for start, size in voids:
        if size>max_size:
            max_size=size
            max_start=start
    return max_start,max_size

def turn_to_void():
    steps_forward,size=biggest_void()
    steps_back=steps-steps_forward
    print "turning to biggest void, back(left)", steps_back, "forward(right)", steps_forward
    if steps_forward<steps_back:
        for i in range(steps_forward + size/2):
            turn_right(turn_time)
            sleep(0.2)
    else:
        for i in range(steps_back - size/2):
            turn_left(turn_time)
            sleep(0.2)

try:
    while True:
        scan()
        do_voids()
        for start, size in voids:
            print "Void starting at ", start, " size ", size

        turn_to_void()

        while get_distance()>object_stop:
            forwards(0.1)

except KeyboardInterrupt:
       print "Cleaning up"
       stop()
       cleanup()
