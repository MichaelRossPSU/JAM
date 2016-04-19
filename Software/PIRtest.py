import RPi.GPIO as GPIO
import time


sensor = 17
relay = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(sensor, GPIO.IN, GPIO.PUD_DOWN)
GPIO.setup(relay, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, False)
pwm = GPIO.PWM(18, 2400)
pwm.start(50)
GPIO.output(relay, False)
previous_state = False
current_state = False
while True:
    time.sleep(0.1)
    previous_state = current_state
    current_state = GPIO.input(sensor)
    if current_state != previous_state:
        new_state = "HIGH" if current_state else "LOW"
        print("GPIO pin %s is %s" % (sensor, new_state))
        GPIO.output(relay, True)
        GPIO.output(18, True)