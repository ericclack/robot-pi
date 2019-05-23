#!/usr/bin/env python

import RPi.GPIO as g
from time import sleep, time

g.setwarnings(False)
g.setmode(g.BOARD)
# Right motor

g.setup(19, g.OUT)
g.setup(21, g.OUT)

# Left motor 
g.setup(26, g.OUT)
g.setup(24, g.OUT)

# LEDs
LEDs = [7,11,18,22]
for led in LEDs:
    g.setup(led, g.OUT)
    g.output(led, 1)

# Define Sonar Pin for Trigger and Echo to be the same
SONAR = 8

# -----------------------------------

def LED_on(i):
    led = LEDs[i]
    g.output(led, 0) # 0 = on!

def LED_off(i):
    led = LEDs[i]
    g.output(led, 1)

def LED_test():    
    for i in range(len(LEDs)):
        LED_on(i)
        sleep(0.5)
        LED_off(i)

def left_forwards():
    g.output(26,0)
    g.output(24,1)

def left_backwards():
    g.output(26,1)
    g.output(24,0)

def right_forwards():
    g.output(21,0)
    g.output(19,1)

def right_backwards():
    g.output(21,1)
    g.output(19,0)

def forwards(s):
    left_forwards()
    right_forwards()
    sleep(s)
    stop()

def backwards(s):
    left_backwards()
    right_backwards()
    sleep(s)
    stop()

def stop():
    for p in [19, 21, 24, 26]:
        g.output(p, 0)

def turn_right(s):
    left_forwards()
    right_backwards()
    sleep(s)
    stop()

def turn_left(s):
    left_backwards()
    right_forwards()
    sleep(s)
    stop()

def get_distance():
    g.setup(SONAR, g.OUT)
    # Send 10us pulse to trigger
    g.output(SONAR, True)
    sleep(0.00001)
    g.output(SONAR, False)
    start = time()
    count = time()
    g.setup(SONAR,g.IN)
    # Now wait for reflection
    while g.input(SONAR)==0 and time()-count<0.1:
        start = time()
    count = time()
    stop = count
    # ...and end of reflection
    while g.input(SONAR)==1 and time()-count<0.1:
        stop = time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound 34000(cm/s) divided by 2
    distance = elapsed * 17000
    return distance


def cleanup():
    g.cleanup()


