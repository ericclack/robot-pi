#!/usr/bin/env python

from robot import *

# Move in squares

for i in range(5):
    turn_right(0.5)
    forwards(0.7)
    turn_right(0.5)
    backwards(0.6)

stop()

cleanup()
