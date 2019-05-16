#!/usr/bin/env python

import RPi.GPIO as g
from time import sleep

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

# ------------------------

# Just move forwards

#turn_right(.1)

for i in range(5):
    turn_right(0.5)
    forwards(0.7)
    turn_right(0.5)
    backwards(0.6)

stop()

g.cleanup()
