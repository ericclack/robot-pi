from robot import *
import time

try:
    while True:
        print "Distance: ", get_distance()
	time.sleep(0.5)

except KeyboardInterrupt:
       print "Cleaning up"
       cleanup()

