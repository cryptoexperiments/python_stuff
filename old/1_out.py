import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
while True:
    print GPIO.input(20)
