import RPi.GPIO as GPIO
import time


pinRelay = 20
delay = 2
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pinRelay, GPIO.OUT)

GPIO.output(pinRelay, True)
time.sleep(delay)
GPIO.output(pinRelay, False)
time.sleep(delay)
