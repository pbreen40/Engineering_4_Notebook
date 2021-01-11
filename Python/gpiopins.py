import RPi.GPIO as GPIO 
from time import sleep 
GPIO.setwarnings(False) # Everything breaks when this is removed
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) # Pin 8 is an output
for x in range(10):   #loop runs 10 times
 GPIO.output(8, GPIO.HIGH) # Turn on
 sleep(1) # Sleep for 1 second
 GPIO.output(8, GPIO.LOW) # Turn off
 sleep(1) # Sleep for 1 second
