import RPi.GPIO as GPIO, sys, threading, time

#use physical pin numbering
GPIO.setmode(GPIO.BOARD)

# Define Sonar Pin for Trigger and Echo to be the same
SONAR = 8

def get_distance():
    GPIO.setup(SONAR, GPIO.OUT)
    # Send 10us pulse to trigger
    GPIO.output(SONAR, True)
    time.sleep(0.00001)
    GPIO.output(SONAR, False)
    start = time.time()
    count=time.time()
    GPIO.setup(SONAR,GPIO.IN)
    # Now wait for reflection
    while GPIO.input(SONAR)==0 and time.time()-count<0.1:
        start = time.time()
    count=time.time()
    stop=count
    # ...and end of reflection
    while GPIO.input(SONAR)==1 and time.time()-count<0.1:
        stop = time.time()
    # Calculate pulse length
    elapsed = stop-start
    # Distance pulse travelled in that time is time
    # multiplied by the speed of sound 34000(cm/s) divided by 2
    distance = elapsed * 17000
    return distance

try:
    while True:
        print "Distance: ", get_distance()
	time.sleep(0.5)

except KeyboardInterrupt:
       print "Cleaning up"
       GPIO.cleanup()

