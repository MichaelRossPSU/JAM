import RPi.GPIO as GPIO
import time


sensor = 17


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) # Set up GPIO using I/O pin numbering
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN) # Sets sensor as input and pulls down to logic 0

# Setup PWM output
GPIO.setup(18, GPIO.OUT) 
GPIO.output(18, False) 
pwm = GPIO.PWM(18, 2400)


while True:
    state = GPIO.input(sensor)
    if state == 0:
    	GPIO.output(18, False)
    	pwm.stop()
    	time.sleep(0.1)
    elif state == 1:
    	print "Intruder!", state
    	pwm.start(50)
    	GPIO.output(18, True)
    	time.sleep(30)